 function updateHeader() {
    var select = document.getElementById("email-select");
    var email = select.options[select.selectedIndex].value;
    var header = document.getElementById("email-header");
    header.innerHTML = "Письма с почты " + email + " будут отображаться ниже";
    }

    var totalEmails = 0;
    var loadedEmails = 0;

    function startLoading() {
        var email = document.getElementById('email-select').value;
        var socket = new WebSocket('ws://localhost:8000/ws/message/');

        socket.onopen = function() {
            socket.send(JSON.stringify({'email': email}));
        };

        socket.onmessage = function(event) {
            var data = JSON.parse(event.data);

            // Обновление общего количества писем
            if (data.total) {
                totalEmails = data.total;
                document.getElementById('total-count').innerText = totalEmails;
            }

            // Обработка сообщения
            if (data.message) {
                addEmailRow(data.message);

                // Увеличение счетчика загруженных писем
                loadedEmails++;
                document.getElementById('loaded-count').innerText = loadedEmails;

                // Обновление прогресс-бара
                updateProgressBar(loadedEmails, totalEmails);
            }
        };
    }

    function updateProgressBar(loaded, total) {
        if (total > 0) {
            const percentage = (loaded / total) * 100;
            const progressBar = document.getElementById("progress-bar");

            // Обновляем ширину прогресс-бара
            progressBar.style.width = percentage + "%";
            progressBar.innerText = Math.round(percentage) + "%";
            progressBar.setAttribute('aria-valuenow', percentage);

            // Если процент больше 0, меняем цвет заливки на синий
            if (percentage > 0) {
                progressBar.style.backgroundColor = "#007bff";  // Синий цвет (Bootstrap "primary")
                progressBar.style.color = "#fff";  // Цвет текста на заливке — белый
            } else {
                // Если процент 0, оставляем белую полосу
                progressBar.style.backgroundColor = "#fff"; // Белая полоса
                progressBar.style.color = "#000"; // Черный текст
            }
        }
    }

    function addEmailRow(message) {
        var tableBody = document.querySelector('#email-table-body');

        var row = document.createElement('tr');

        var dateCell = document.createElement('td');
        dateCell.innerText = message.letter_date;

        var fromCell = document.createElement('td');
        fromCell.innerText = message.letter_from;

        var titleCell = document.createElement('td');
        var titleText = message.letter_title.length
         > 30 ? message.letter_title.slice(0, 30) + '...' : message.letter_title;
        titleCell.innerText = titleText;

        var bodyCell = document.createElement('td');
        var bodyText = message.letter_body.length
         > 50 ? message.letter_body.slice(0, 50) + '...' : message.letter_body;
        bodyCell.innerText = bodyText;

        row.appendChild(dateCell);
        row.appendChild(fromCell);
        row.appendChild(titleCell);
        row.appendChild(bodyCell);

        tableBody.appendChild(row);
    }