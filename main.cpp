#include <iostream>
#include <cmath>

//constants
learning_rate = 0.01;

float activation(float x){
  if(x >= 0 && x <= 1){
    return x;
  }else if(x < 0){
    return 0.0001 * x;
  }else{
    return 1 + 0.0001 * (x - 1);
  }
}

float deriv_activation(x){
  if(x >= 0 && x <= 1){
    return 1;
  }else{
    return 0.0001;
  }
}

int main(){

}
