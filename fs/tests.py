from django.test import TestCase

# Create your tests here.

# Ajouter agence avec de joli furmulaire
""" {% extends 'default/index.html'%}

{% block content %}



<div class="row">
  <div class="col-md-12">
    <div class="card card-body">
      <div class="card-header">
        <h3>Ajouter une agence</h3>
      </div>

      <div class="card-body">

        <form action="{% url 'ajouter_agence' %}" method="POST">
          <div class="row g-3">
            {% csrf_token %}
            <div class="col-md-6">
              <label for="" class="form-label">Nom de l'agence:</label>
              <div class="form-group">
                {{form.nom_agence}}
              </div>

            </div>

            <div class="col-md-6">
              <label for="" class="form-label">institution</label>
              {{form.entreprise}}

            </div>

            <div class="col-md-6">
              <label for="" class="form-label">contact</label>
              <div class="form-group">
                {{form.contact}}
              </div>
            </div>

            <hr>

            <div class="col-md-6">
              <label for="" class="form-label">Mot de passe</label>
              <div class="form-group">
                {{form2.password}}
              </div>

              <!-- <input type="password" name="password" class="input-bx" placeholder=""> -->

            </div>

            <div class="col-md-6">
              <label for="" class="form-label">Confirmer le mot de passe</label>
              <div class="form-group">
                {{form2.passwordCheck}}
              </div>
              <!-- <input type="password" name="passwordCheck" class="input-bx" placeholder=""> -->
            </div>


          </div>
            <br/>
        <hr>

        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
          <button type="submit" class="btn btn-primary">AJOUTER</button>
        </div>


        </form>


      </div>

    </div>
  </div>
</div>



{% endblock %} """