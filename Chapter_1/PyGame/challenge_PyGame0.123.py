import pygame
from M_Dawson_Home_Work.Chapter_1.PyGame.settings import *  # загрузка функций всего экшена
import M_Dawson_Home_Work.Chapter_1.PyGame.functions as f  # тут все классы, кнопка, поле ввода, картинка
from pygame.sprite import Group


def run_main():
    pygame.init()
    ai_setting = Settings()  # разросся, можно и поделить.
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Выбор мороженного и ко')
    # Создание кнопок-интерфейса.
    button = Button(screen, 'Очистить', width_x=200, rect_width=440)
    check_button = Button(screen, '#1', rect_height=380)
    check_button2 = Button(screen, '#2', rect_height=330)
    check_button3 = Button(screen, '#3', rect_height=280)
    check_button4 = Button(screen, '#4', rect_height=230)
    # создали группу, засунули туда все кнопки
    gui = Group()
    gui.add(button, check_button, check_button2, check_button3, check_button4 )
    # создали картинку
    image_all= Image(screen)
    # создали группу, поля ввода и добавили их в группу
    input_boxis = Group()
    input_box = InputBox(screen)
    input_box1 = InputBox(screen, rect_height=65)
    input_boxis.add(input_box, input_box1)
    # Запуск основного цикла игры.
    while True:
        f.check_events(ai_setting, screen, gui, image_all, input_boxis)
        f.update_screen(ai_setting, screen, gui, image_all, input_boxis)

if __name__ == '__main__':
    run_main()
    pygame.quit()
