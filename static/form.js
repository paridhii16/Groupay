document.getElementById("entry-form").addEventListener("submit", function (event) {
    event.preventDefault();
    // Registration logic goes here

    window.location.href = "HomePage.html";
    // Registration logic goes here
});

document.getElementById("paidBy").addEventListener("change", function () {
    var paidBy = this.value;
    var groupMembersContainer = document.getElementById("groupMembersContainer");
    groupMembersContainer.innerHTML = "";

    var groupMembers = ["Siya", "Diya", "Rohan", "Jay", "Virat", "Maaya", "Piya", "Aryan", "Meera", "Ashmi"];

    if (paidBy !== "") {
        var label = document.createElement("label");
        label.textContent = "Group Members:";
        groupMembersContainer.appendChild(label);
        groupMembersContainer.appendChild(document.createElement("br"));
    }

    groupMembers.forEach(function (member) {
        if (member !== paidBy) {
            var container = document.createElement("div");
            container.classList.add("checkbox-label"); // Add CSS class to the container

            var checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.id = member.replace(" ", "").toLowerCase();
            checkbox.name = "groupMembers";
            checkbox.value = member;
            container.appendChild(checkbox);

            var label = document.createElement("label");
            label.setAttribute("for", checkbox.id);
            label.textContent = member;
            container.appendChild(label);

            groupMembersContainer.appendChild(container);
        }
    });
});

/* 
















*/

document.addEventListener('DOMContentLoaded', () => {
    const entryForm = document.querySelector('#entry-form');
    const submitBtn = entryForm.querySelector('button[type="submit"]');

    submitBtn.addEventListener('click', (event) => {
        event.preventDefault(); // prevent the form from submitting

        // perform form validation here

        // redirect to homepage
        window.location.href = '/';
    });
});
