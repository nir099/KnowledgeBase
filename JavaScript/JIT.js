/**
 * Optimization and de-optimization in JIT 
 */

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, '9', 0, 1, 2, 3]

let sum = 0

array.map(item => {
    sum += item
    console.log(sum)
})