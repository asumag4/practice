class Calculator {
    
    /** 
     * @param {number} value
     */
    constructor(value) {
        this.val = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        this.val += value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        this.val -= value;
        return this;   
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
        this.val *= value;
        return this;    
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value !== 0) {
            this.val /= value;
            return this;
        } else {
            throw new Error("Division by zero is not allowed");
        }
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.val = Math.pow(this.val, value);
        return this;
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        return this.val;
    }
}

console.log(new Calculator(10).add(5).subtract(7).getResult()) // 8 
console.log(new Calculator(20).divide(0).getResult())

/*
======================================================
BEST SOLUTION
======================================================
*/

class Calculator {
    
    /** 
     * @param {number} value
     */
    constructor(value) {
        this.v=value;
        this.err=null;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        this.v+=value;
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        this.v-=value
        return this;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
         this.v*=value;
        return this
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value ==0) this.err="Division by zero is not allowed"; // Shortcut; 
        //  1. this.err!! 
        //  2. Instead of deep assessment (===), do a shallow assessment (==)
        this.v/=value;
        return  this
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        this.v**=value;
        return this
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        if (this.err) return this.err
        return this.v
    }
}