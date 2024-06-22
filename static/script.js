document.addEventListener('DOMContentLoaded', () => {
    const positions = document.querySelectorAll('.position');
    const playerCards = document.querySelectorAll('.player-card');

    playerCards.forEach(card => {
        card.addEventListener('dragstart', dragStart);
    });

    positions.forEach(position => {
        position.addEventListener('dragover', dragOver);
        position.addEventListener('drop', drop);
    });

    function dragStart(e) {
        e.dataTransfer.setData('text/plain', e.target.id);
    }

    function dragOver(e) {
        e.preventDefault();
    }

    function drop(e) {
        e.preventDefault();
        const id = e.dataTransfer.getData('text');
        const draggableElement = document.getElementById(id);
        const dropzone = e.target;

        if (dropzone.children.length > 0) {
            dropzone.removeChild(dropzone.children[0]);
        }

        dropzone.appendChild(draggableElement);
    }
});
