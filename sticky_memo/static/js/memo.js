// DOM 요소
const $modalWrap = document.querySelector(".modal-wrap");
const $newBtn = document.querySelector(".new-btn");
const $closeBtn = document.querySelector(".close-btn");
const $openBtn = document.querySelector(".open-btn");
const $deleteBtn = document.querySelector(".delete-btn");
const $title = document.querySelector(".title");

const remove = () => {
    $modalWrap.classList.remove("hidden");
};

const 이석 = () => {
    $modalWrap.classList.add("hidden");
};

// title 색깔바꾸기
$title.classList.add("change-color")

// .new-btn 클릭시, .modal-wrap의 hidden 클래스 없애기
$newBtn.addEventListener("click", () => {
    remove();
});

// .close-btn 클릭시, .modal-wrap에 hidden 클래스 추가
$closeBtn.addEventListener("click", () => {
    이석();
})

// .open-btn 클릭시, .modal-wrap의 hidden 클래스 없애기
$openBtn.addEventListener("click", () => {
    remove();
})

// .delete-btn 클릭시, 삭제 여부 물어보는 창 띄워주기
$deleteBtn.addEventListener("click", () => {
    confirm("저에게 10억을 입금하시겠습니까?")
})
