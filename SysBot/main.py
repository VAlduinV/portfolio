import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from SysBot.models.Form import Form
from SysBot.secrets.config import bot_token, GROUP_CHAT_ID
from SysBot.Database.database import *
import html

bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types=['photo'])
async def get_photo_id(message: types.Message):
    photo_id = message.photo[0].file_id
    print(f'Photo ID: {photo_id}')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    logging.info('/start command received')
    await bot.send_photo(
        chat_id=message.chat.id,
        photo='AgACAgIAAxkBAAIBSmSIsHpNS4qlRiyRoUsjUrIidjd2AAIjyzEbjTVASNjpkscPYuOGAQADAgADcwADLwQ',
        caption='👋Привет! Я бот для системных администраторов.'
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text='Пожалуйста, выбери отдел:',
        reply_markup=generate_department_markup()
    )


@dp.callback_query_handler(lambda call: call.data.startswith('department_'))
async def handle_department_selection(call: types.CallbackQuery, state: FSMContext):
    await call.answer()  # Ответ на callback запрос
    department = call.data.split('_')[1]
    await state.update_data(department=department)
    await bot.send_message(call.message.chat.id, f'Вы выбрали отдел: {department}. Введите номер ПК:👈')
    await Form.pc_number.set()


@dp.message_handler(state=Form.pc_number)
async def handle_pc_number(message: types.Message, state: FSMContext):
    pc_number = message.text
    await state.update_data(pc_number=pc_number)
    await state.update_data(user_full_name=message.from_user.full_name)
    await state.update_data(user_email=message.from_user.username)
    await bot.send_message(
        message.chat.id,
        'Выберите категорию проблемы:',
        reply_markup=generate_problem_category_markup()
    )
    await Form.next()


@dp.callback_query_handler(lambda call: call.data.startswith('problem_category_'), state=Form.problem_category)
async def handle_problem_category_selection(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    problem_category = call.data.split('_')[2]
    await state.update_data(problem_category=problem_category)
    if problem_category == 'Other':
        await bot.send_message(call.message.chat.id, 'Расскажите про свою проблему:✍️')
        await Form.next()
    else:
        await bot.send_message(call.message.chat.id,
                               'Вы уверены, что хотите отправить сообщение? (да/нет)')  # подтверждение отправки
        await Form.confirm.set()  # переходим к состоянию подтверждения


@dp.message_handler(state=Form.description)
async def handle_description(message: types.Message, state: FSMContext):
    user_description = message.text
    await state.update_data(description=user_description)
    await bot.send_message(
        message.chat.id,
        'Вы уверены, что хотите отправить сообщение? (да/нет)'  # подтверждение отправки
    )
    await Form.confirm.set()  # переходим к состоянию подтверждения


@dp.message_handler(state=Form.confirm)
async def handle_confirmation(message: types.Message, state: FSMContext):
    confirmation = message.text.lower()
    if confirmation in ('да', 'yes'):
        try:
            data = await state.get_data()
            pc_number = data.get('pc_number')  # Получение номера ПК из state
            user_email = data.get('user_email')
            user_info = f"🖥️<b>Пользователь {html.escape(data['user_full_name'])}: @{user_email}</b> нуждается в вашей помощи🖥️\n" \
                        f"🚪Отдел: {html.escape(data['department'])}✍️\n💻Номер ПК: {pc_number}💻"  # Включение номера ПК в информацию о пользователе
            problem_info = f"👉Пользователь имеет следующую проблему из категории: {html.escape(data['problem_category'])}👈"
            description = data.get('description')
            description_info = f"<b>**Дополнительное описание:**</b>\n- {html.escape(description.strip())}\n" if description else ""

            sent_message = await bot.send_message(
                GROUP_CHAT_ID,
                f"{'=' * 55}\n"
                f"{user_info}\n"
                f"{problem_info}\n"
                f"{description_info}"
                f"{'=' * 55}",
                parse_mode=types.ParseMode.HTML
            )
            await state.update_data(message_id=sent_message.message_id)
            await bot.send_message(message.chat.id, 'Ваше сообщение успешно доставлено!✅')

            # Save user data to the database, including PC number
            user_full_name = data.get('user_full_name')
            department = data.get('department')
            problem_category = data.get('problem_category')
            save_user_data_to_db(user_full_name, user_email, department, problem_category,
                                 pc_number)  # Добавление номера ПК в базу данных

            await state.finish()
        except Exception as e:
            logging.error(f"Error sending message: {e}")
            await bot.send_message(message.chat.id, 'Произошла ошибка при отправке сообщения.')
            await state.finish()
    elif confirmation in ('нет', 'no'):
        await bot.send_message(message.chat.id, 'Отправка сообщения отменена.')
        await state.finish()
    else:
        await bot.send_message(message.chat.id, 'Пожалуйста, ответьте "да" или "нет".')


def generate_department_markup():
    markup = types.InlineKeyboardMarkup(row_width=3)
    dior_button = types.InlineKeyboardButton('Пидорас Михуило👈', callback_data='department_Pidoras Mihuilo')
    monro_button = types.InlineKeyboardButton('Пидорас Дима👌', callback_data='department_Dima')
    hr_fiz_button = types.InlineKeyboardButton('Пидорас глекген/микола👈', callback_data='department_Pidoras Gleckgen/mikola')
    markup.add(dior_button, monro_button, hr_fiz_button)
    return markup


def generate_problem_category_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    ram_button = types.InlineKeyboardButton('ОЗУ', callback_data='problem_category_RAM')
    hdd_ssd_button = types.InlineKeyboardButton('SSD/HDD', callback_data='problem_category_SSD/HDD')
    motherboard_button = types.InlineKeyboardButton('Материнская плата', callback_data='problem_category_Motherboard')
    other_button = types.InlineKeyboardButton('Другое', callback_data='problem_category_Other')
    markup.add(ram_button, hdd_ssd_button, motherboard_button, other_button)
    return markup


if __name__ == '__main__':
    from aiogram import executor
    print(
        '''
       _____                           _             _        
      / ____|                /\       | |           (_)       
     | (___   _   _  ___    /  \    __| | _ __ ___   _  _ __  
      \___ \ | | | |/ __|  / /\ \  / _` || '_ ` _ \ | || '_ \ 
      ____) || |_| |\__ \ / ____ \| (_| || | | | | || || | | |
     |_____/  \__, ||___//_/    \_\\__,_||_| |_| |_||_||_| |_|
               __/ |                                          
              |___/                                            
        '''
    )
    data_base()
    executor.start_polling(dp, skip_updates=True)
