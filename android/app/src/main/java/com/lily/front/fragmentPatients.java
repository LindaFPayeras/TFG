package com.lily.front;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;


import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class fragmentPatients extends Fragment {
    private RecyclerView recyclerView;
    private RecyclerView.Adapter adapter;
    private RecyclerView.LayoutManager layoutManager;

    private View view;
    private List<patientCard> patientsList = new ArrayList<>();

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){

        fillPatientsList();
        view = inflater.inflate(R.layout.fragment_patients, container, false);

        recyclerView = view.findViewById(R.id.patientList);
        recyclerView.setHasFixedSize(true);

        layoutManager = new LinearLayoutManager(getContext());
        recyclerView.setLayoutManager(layoutManager);

        adapter = new patientAdapter(patientsList);
        recyclerView.setAdapter(adapter);

        return view;
    }

    private void fillPatientsList(){ // Hardcoded por ahora
        patientCard patientCard0 = new patientCard("Belen Sanchez","24-03-2026","happy");
        patientCard patientCard1 = new patientCard("Ana García","30-03-2026","anxiety");
        patientCard patientCard2 = new patientCard("Ariadna Perez","01-04-2026","anxiety");

        patientsList.addAll(
                Arrays.asList(patientCard0,patientCard1,patientCard2)
        );

    }

}