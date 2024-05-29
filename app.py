from flask import Flask, render_template, request, jsonify

from utils.fan_utils import FanUtils
from utils.gpio_utils import GpioUtils

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/control', methods=['POST'])
def control():
    data = request.json
    action = data['action']
    gpio_group = int(data['group'])  # 确保gpio数据是整数型
    gpio_pin = int(data['pin'])  # 确保gpio数据是整数型

    # 确保gpio值在一个安全的范围内
    # if gpio_pin not in available_gpio_pins:
    #     return jsonify({'status': 'error', 'message': 'Invalid GPIO pin'})

    if action == "on":
        # 你的GPIO打开操作代码
        GpioUtils.set_direction(gpio_group, gpio_pin, 1)
        success, message = GpioUtils.set_value(gpio_group, gpio_pin, 1)
    elif action == "off":
        # 你的GPIO关闭操作代码
        GpioUtils.set_direction(gpio_group, gpio_pin, 1)
        success, message = GpioUtils.set_value(gpio_group, gpio_pin, 0)
    else:
        return jsonify({'status': 'error', 'message': 'Invalid action'})

    # 在成功的情况下返回消息
    return jsonify({'status': 'success', 'message': message})


@app.route('/fan-speed', methods=['POST'])
def fan_speed():
    data = request.json
    speed = int(data['speed'])
    # 检查速度值
    if speed < 0 or speed > 100:
        return jsonify({'message': 'Invalid speed value'}), 400

    # 设置风扇为手动模式
    success, message = FanUtils.set_pwm_mode(0)
    if not success:
        return jsonify({'message': 'Failed to set PWM mode', 'details': message}), 500

    # 设置PWM的占空比
    success, message = FanUtils.set_pwm_duty_ratio(speed)
    if not success:
        return jsonify({'message': 'Failed to set fan speed', 'details': message}), 500

    return jsonify({'message': f'Fan speed set to {speed}%'}), 200


@app.route('/fan-status', methods=['GET'])
def fan_status():
    success, pwm_mode = FanUtils.get_pwm_mode()
    if not success:
        return jsonify({'status': 'error', 'message': 'Failed to get fan mode', 'details': pwm_mode}), 500

    success, pwm_duty_ratio = FanUtils.get_pwm_duty_ratio()
    if not success:
        return jsonify({'status': 'error', 'message': 'Failed to get duty ratio', 'details': pwm_duty_ratio}), 500

    return jsonify({
        'status': 'success',
        'pwm_mode': pwm_mode.split(' : ')[-1],
        'pwm_duty_ratio': pwm_duty_ratio.split(' : ')[-1]
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
