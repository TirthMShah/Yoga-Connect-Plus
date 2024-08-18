function unhide(post) {
    post.removeAttribute('hidden');
    btn1 = document.getElementById('btn_for_text_post');
    btn2 = document.getElementById('btn_for_image_post');
    btn1.setAttribute("hidden", true);
    btn2.setAttribute("hidden", true);
}

// document.getElementById("submit_like_dislike").addEventListener("click", function () {
//     document.getElementById("like_dislike_form").submit();
// });