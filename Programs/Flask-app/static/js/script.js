function addSkill() {
    var skillsDiv = document.getElementById('skills');
    var newInputDiv = document.createElement('div');
    newInputDiv.className = 'd-flex flex-row align-items-center mb-2';
    
    var input = document.createElement('input');
    input.type = 'text';
    input.name = 'skills[]';
    input.className = 'form-control w-50 me-2';
    newInputDiv.appendChild(input);

    // Assuming there's only one button, get the current button and its parent div
    var currentButton = document.querySelector('#skills button');
    var buttonParentDiv = currentButton.parentNode;
    
    // Remove the button from its current position
    buttonParentDiv.removeChild(currentButton);

    newInputDiv.appendChild(currentButton);

    // Add the new input div to the skills container
    skillsDiv.appendChild(newInputDiv);
}
