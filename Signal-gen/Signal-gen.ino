int F = 2;                                                   //frequency of the signal
int Fs = 500;                                                //sampling frequency
int n = 50000;                                                 //number of samples
float t;                                                     //Time instance
int sampling_interval;
byte samples[500];                                           // to store the samples

void setup() {

  pinMode(10, OUTPUT);
  for (int n = 0; n < 500; n++)
  {
    t = (float) n / Fs;                                       
    samples[n] = (byte) (127.0 * sin(2 * 3.14 * t) + 127.0 ); 
  }
  sampling_interval = 1000 / (F * n);                      
  
}

void loop() {
  for (int j = 0; j < 500; j++) {
    Serial.print(j);
    analogWrite(10, samples[j]);
    delayMicroseconds(sampling_interval);                      //time interval
  }
}