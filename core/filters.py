from django_filters import rest_framework as filters


class IsPlotFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to get their own objects

    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(plot_owner=request.user)