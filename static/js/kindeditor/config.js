KindEditor.ready(function (K) {
    //用什么标签显示
    window.editor = K.create('textarea[name=content]', {
        width: '800px',
        height: '200px',
        uploadJson: '/admin/upload/kindeditor',
    });
});
