$( document ).ready(function() {
    function toggleChevron(e) {
        $(e.target)
            .prev('.panel-heading')
            .find("i.indicator")
            .toggleClass('glyphicon-folder-open glyphicon-folder-close');
    }
    $('#accordion').on('hidden.bs.collapse', toggleChevron);
    $('#accordion').on('shown.bs.collapse', toggleChevron);


    function blogToggleChevron(e) {
        $(e.target)
            .prev('.blog-panel')
            .find("i.indicator")
            .toggleClass('glyphicon-folder-open glyphicon-folder-close');
    }
    $('#accordion-blog').on('hidden.bs.collapse', blogToggleChevron);
    $('#accordion-blog').on('shown.bs.collapse', blogToggleChevron);


    function probSolToggleChevron(e) {
    $(e.target)
        .prev('.prob-sol-panel')
        .find("i.indicator")
        .toggleClass('glyphicon-folder-open glyphicon-folder-close');
    }
    $('#accordion-problem-solution').on('hidden.bs.collapse', probSolToggleChevron);
    $('#accordion-problem-solution').on('shown.bs.collapse', probSolToggleChevron);

});