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
            let tr = document.createElement('tr');
            let td = document.createElement('td');
            td.innerText = i;
            tr.appendChild(td);
            td = document.createElement('td');
            td.innerText = film.title == film.title_ru ? '' : film.title;
            tr.appendChild(td);

            td = document.createElement('td');
            td.innerText = film.title_ru;
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
            td.appendChild(editButton);
        
            let deleteButton = document.createElement('button');
            deleteButton.innerText = 'Delete';
            deleteButton.onclick = function() {deleteFilm(i, film.title)}
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