from pyscript import document, display

# Get Values
def calculate_grade(e): 
    grade1 = float(document.getElementById("grade1").value)
    grade2 = float(document.getElementById("grade2").value)
    grade3 = float(document.getElementById("grade3").value)
    grade4 = float(document.getElementById("grade4").value)
    grade5 = float(document.getElementById("grade5").value)
    grade6 = float(document.getElementById("grade6").value)

 # Divide and Conquer
    avg = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6)/6

    final_grade = avg

 # Display Result
    display(f"Science: {grade1}<br>Math: {grade2}<br>English: {grade3}<br>Filipino: {grade4}<br>ICT: {grade5}<br>PE: {grade6}", target="output")   
 
    display(f"Your General Weighted Average is: {final_grade:.2f}", target="final_grade")