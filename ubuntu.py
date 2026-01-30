print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("hello 1,2,3,4")
var primeArray = [];

function PrimeCheck(candidate){
    
    var isPrime = true;
    var i = 2;
    while (i<candidate){
        if (candidate%i === 0){
            i = candidate;
            isPrime = false;
        }
    i++;    
    }
    return isPrime;
}

var numPrimes = prompt("How many primes?");
var j = 2;
while (primeArray.length<numPrimes){
    if (PrimeCheck(j)){
        primeArray.push(j);
    }
    j++;
}


console.log(primeArray);
 isPrime = true;
  for(var i = 2; i < candidate && isPrime; i++){
    if(candidate%i === 0){
      isPrime = false;
    } else {
      isPrime = true;
    }
  }
  if(isPrime){
    primeArray.push(candidate);
  }
  return primeArray;
}
