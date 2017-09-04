from django.shortcuts import render, get_object_or_404
from .models import Doctor_Referral
from django.views.generic import DetailView, ListView

# Create your views here.
class Doctor_Referral_DetailView(DetailView):
    # template_name =  "doctor_referral/detail_view.html"
    queryset = Doctor_Referral.objects.all()
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Doctor_Referral.objects.get(id=pk)

class Doctor_Referral_ListView(ListView):
    # template_name = "doctor_referral/list_view.html"
    queryset = Doctor_Referral.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(Doctor_Referral_ListView, self).get_context_data(*args, **kwargs)
        return context


# def doctor_referral_detail_view(request, id=1):
#     obj = Doctor_Referral.objects.get(id=id)
#     context = {
#         "object":obj
#     }
#     return render(request, "doctor_referral/detail_view.html", context)

# def doctor_referral_list_view(request):
#     queryset = obj = Doctor_Referral.objects.all()
#     context = {
#         "object_list":queryset
#     }
#     return render(request, "doctor_referral/list_view.html", context)