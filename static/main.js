function FillFilmList() {
    const url = '/lab7/rest-api/films/'; 
    
    fetch(url)
    .then(function(response) {
        return response.json()
    })  
    .then(function(film_list) {
        const body = document.getElementById('film-list'); 
        body.innerHTML = '';
        for (let i=0; i<film_list.length; i++) {
            const film = film_list[i];
            const id = film['id'];
            let tr = document.createElement('tr');
            let td = document.createElement('td');
            td.innerText = id;
            tr.appendChild(td);

            td = document.createElement('td');
            let title = film.title_ru;
            title +=  film.title == film.title_ru ? '' : ' (' + film.title + ')'
            td.innerText = title ;
            tr.appendChild(td);


            td = document.createElement('td');    
            td.innerText = film.year;
            tr.appendChild(td);     

            td = document.createElement('td');    
            td.innerText = film.description; 
            tr.appendChild(td);

            td = document.createElement('td');

            let editButton = document.createElement('button');
            editButton.innerText = 'Edit';
            editButton.onclick = function() {editFilm(id)}
            td.appendChild(editButton);
        
            let deleteButton = document.createElement('button');
            deleteButton.innerText = 'Delete';
            deleteButton.onclick = function() {deleteFilm(id, film.title)}
            td.appendChild(deleteButton);

            tr.appendChild(td); /// добавляем строчку 

            body.appendChild(tr);
        
        }
    })
}   

function deleteFilm(id, title) {
    if (!confirm(`Вы действительно хотите удалить фильм "${title}"?`)) {
        return;
    }
    const url = '/lab7/rest-api/films/' + id; 
    fetch(url, {method: 'DELETE'})
    .then(function() {
        FillFilmList();
    })
}

function showModal(){
    document.getElementById('title-error').innerText = '';
    document.getElementById('title_ru-error').innerText = '';
    document.getElementById('year-error').innerText = '';
    document.getElementById('description-error').innerText = '';    

    const modal = document.querySelector('.modal');
    modal.style.display = 'block';
}
function hideModal(){
    const modal = document.querySelector('.modal');
    modal.style.display = 'none';
}   

function cancel(){
    hideModal();
}

function addFilm() {
    
    document.getElementById('title').value = '';
    document.getElementById('title_ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    document.getElementById('id').value = '';
    showModal();
}

function SendFilm() {
    const id = document.getElementById('id').value;
    const url = '/lab7/rest-api/films/' + id;
    const method = id ==='' ?  'POST' : 'PUT'; 
    fetch(url, {
        method: method,
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify({
            title: document.getElementById('title').value,
            title_ru: document.getElementById('title_ru').value,
            year: document.getElementById('year').value,
            description: document.getElementById('description').value
        })
    })
    .then(function(response) {
        if (response.ok) {
            hideModal();
            FillFilmList();
            return {}
        } else {
            return response.json()
        }
    })
    .then(function(error) {
        if (error) {
            if (error.title) {
                document.getElementById('title-error').innerText = error.title;
            }
            if (error.title_ru) {
                document.getElementById('title_ru-error').innerText = error.title_ru;
            }
            if (error.year) {
                document.getElementById('year-error').innerText = error.year;
            }
            if (error.description) {
                document.getElementById('description-error').innerText = error.description;
            }
        }
    });
}

function editFilm(id) {
    fetch('/lab7/rest-api/films/' + id)
    .then(function(response) {
        return response.json()
    })  
    .then(function(film) {
        document.getElementById('title').value = film.title;
        document.getElementById('title_ru').value = film.title_ru;
        document.getElementById('year').value = film.year;
        document.getElementById('description').value = film.description;
        document.getElementById('id').value = id;
    
        showModal();
    })
}
