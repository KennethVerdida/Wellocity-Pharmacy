  /* global $ */
  /* eslint-env es6 */
  /* eslint-disable */
  $('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })