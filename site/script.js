num1 = document.getElementById("number1")
num2 = document.getElementById("number2")
btn = document.getElementById("btn")
p = document.getElementsByClassName("copy")[0]
max = parseInt(num1.max)

this.onload = ()=>{
    num1.focus()
    num1.select()
}

num1.oninput = (e)=>{
    if (p.style.display != 'none') p.style.display = 'none'
    num1.value = parseInt(num1.value)
    if(parseInt(num1.value)>max) num1.value = num1.value.slice(0, 13)
    num2.value = separator(num1.value)    
}

keys = ['-', 'e', '+', 'E']

num1.onkeydown = (e)=>{
    if(keys.includes(e.key)) e.preventDefault();
}

num2.onclick = (e) => {
    if(num1.value == "" || 0) return
    num2.setSelectionRange(0, num2.length)
    num2.select()
    navigator.clipboard.writeText(num2.value)
    console.log("COPIED | " + num2.value)
    p.style.display = "initial"
}
