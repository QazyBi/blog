tinymce.init({
  selector: 'textarea#basic-example',
  height: 500,
  menubar: false,
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table paste codesample help wordcount'
  ],
  toolbar: 'undo redo | formatselect | ' +
  'bold underline | fontselect fontsizeselect | alignleft aligncenter ' +
  'alignright | outdent indent | insertfile image | forecolor | code codesample | bullist numlist outdent indent | ' +
  'removeformat | help',
  content_css: '//www.tiny.cloud/css/codepen.min.css'
});
