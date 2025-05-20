from w1thermsensor import W1ThermSensor, SensorNotReadyError, ResetValueError
import time

def read_temperature(retries=5, delay=1):
    sensor = W1ThermSensor()
    for i in range(retries):
        try:
            temp = sensor.get_temperature()
            # 리셋값(85°C) 방지
            if abs(temp - 85.0) < 0.01:
                raise ResetValueError(sensor.id)
            return round(temp, 2)
        except (SensorNotReadyError, ResetValueError):
            time.sleep(delay)
    raise RuntimeError("센서 응답 없음")

if __name__ == "__main__":
    t = read_temperature()
    print(f"수온: {t}°C")
