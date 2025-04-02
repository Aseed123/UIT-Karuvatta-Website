from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class IndexView(TemplateView):

    template_name="index.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)


class AboutView(TemplateView):

    template_name="about.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)


class BscComputerScienceView(TemplateView):

    template_name="bsc_comp.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    

class BcaComputerScienceView(TemplateView):

    template_name="bca_comp.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)


class BcomFinanceView(TemplateView):

    template_name="bcom_finance.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)


class BcomCooperationView(TemplateView):

    template_name="bcom_cop.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    
    
class ComputerLabView(TemplateView):

    template_name="computer_lab.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)


class OtherStaffsView(TemplateView):

    template_name="other_staffs.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    

class AchievementsView(TemplateView):

    template_name="achievements.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    

class ClubsView(TemplateView):

    template_name="clubs.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
    

class NssView(TemplateView):

    template_name="nss.html"

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)