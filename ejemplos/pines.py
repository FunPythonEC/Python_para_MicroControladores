Empezando con micropython en ESP8266/32
from machine import Pin

Salida (leds, buzzer, reles)
pin = Pin(0, Pin.OUT)

p0.on()             
p0.off()            
p0.value(1)         

entrada (botones)

pin = Pin(2, Pin.IN) 
p2 = Pin(2, Pin.IN) 
print(p2.value())   


from machine import Pin, PWM

pwm0 = PWM(Pin(0))      # create PWM object from a pin
pwm0.freq()             # get current frequency
pwm0.freq(1000)         # set frequency
pwm0.duty()             # get current duty cycle
pwm0.duty(200)          # set duty cycle
pwm0.deinit()           # turn off PWM on the pin

pwm2 = PWM(Pin(2), freq=20000, duty=512) # create and configure in one go


PWM

from machine import Pin, PWM

pwm = PWM(Pin(0))
pwm.freq(500)
pwm.duty(100)

ADC 

from machine import ADC

adc = ADC(Pin(32))
adc.read()  



