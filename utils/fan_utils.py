#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: @Suroy
@site: https://suroy.cn/
@email: suroy@qq.com
@time: 2024/5/30 3:21 AM
"""
import subprocess


class FanUtils:
    @staticmethod
    def set_pwm_mode(mode):
        """设置风扇模式 (0: 手动, 1: 自动)"""
        try:
            subprocess.run(f'sudo npu-smi set -t pwm-mode -d {mode}', shell=True, check=True)
            return True, "Success"
        except subprocess.CalledProcessError as e:
            return False, str(e)

    @staticmethod
    def set_pwm_duty_ratio(speed):
        """设置风扇调速比"""
        try:
            subprocess.run(f'sudo npu-smi set -t pwm-duty-ratio -d {speed}', shell=True, check=True)
            return True, "Success"
        except subprocess.CalledProcessError as e:
            return False, str(e)

    @staticmethod
    def get_pwm_mode():
        """获取当前风扇模式"""
        try:
            result = subprocess.run('sudo npu-smi info -t pwm-mode', shell=True, check=True, capture_output=True,
                                    text=True)
            mode = result.stdout.strip()
            return True, mode
        except subprocess.CalledProcessError as e:
            return False, str(e)

    @staticmethod
    def get_pwm_duty_ratio():
        """获取当前风扇调速比"""
        try:
            result = subprocess.run('sudo npu-smi info -t pwm-duty-ratio', shell=True, check=True, capture_output=True,
                                    text=True)
            duty_ratio = result.stdout.strip()
            return True, duty_ratio
        except subprocess.CalledProcessError as e:
            return False, str(e)
