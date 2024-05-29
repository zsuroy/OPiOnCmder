#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: @Suroy
@site: https://suroy.cn/
@email: suroy@qq.com
@time: 2024/5/30 2:37 AM
"""

import subprocess


class GpioUtils:
    @staticmethod
    def execute_command(command):
        try:
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
            return True, "Success"
        except subprocess.CalledProcessError as e:
            return False, f"Command failed: {e}"

    @classmethod
    def set_direction(cls, group, pin, direction):
        command = f"gpio_operate set_direction {group} {pin} {direction}"
        return cls.execute_command(command)

    @classmethod
    def get_direction(cls, group, pin):
        command = f"gpio_operate get_direction {group} {pin}"
        success, message = cls.execute_command(command)
        if success:
            # 在这里解析输出以获取方向，暂时返回message原信息
            return True, message
        else:
            return False, message

    @classmethod
    def set_value(cls, group, pin, value):
        command = f"gpio_operate set_value {group} {pin} {value}"
        return cls.execute_command(command)

    @classmethod
    def get_value(cls, group, pin):
        command = f"gpio_operate get_value {group} {pin}"
        success, message = cls.execute_command(command)
        if success:
            # 在这里解析输出以获取值，暂时返回message原信息
            return True, message
        else:
            return False, message
