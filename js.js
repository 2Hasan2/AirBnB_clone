function factorial(n) {
	if (n === 0) {
		return 1;
	} else {
		return n * factorial(n - 1);
	}
}

// Example usage:
let number = 999;
console.log(`Factorial of ${number} is ${factorial(number)}`);
