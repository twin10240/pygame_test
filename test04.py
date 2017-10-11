# Error : import 대상은 모듈(*.py)이어야 한다.
# package(디렉토리)를 import할 수도 있다.
# 단, package(디렉토리)에 __init__.py가 있으면...

# import pygame.sound.echo.test_echo


from pygame.sound.echo import test_echo

test_echo()
