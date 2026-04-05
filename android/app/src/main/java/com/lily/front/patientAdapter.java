package com.lily.front;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class patientAdapter extends RecyclerView.Adapter<patientAdapter.ViewHolder>{
    List<patientCard> patientsList;
    Context context;

    public patientAdapter(List<patientCard> patientsList) {
        this.patientsList = patientsList;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {

        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_card_patient, parent, false);

        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        holder.nameSurname.setText(patientsList.get(position).getNameSurname());
        holder.lastMessage.setText(patientsList.get(position).getLastMessage());
        holder.lastEmotion.setText(patientsList.get(position).getLastEmotion());
       // holder.profilePicture.setImageResource(patientsList.get(position).getProfilePicture());
    }

    @Override
    public int getItemCount() {
        return patientsList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder{

        // ImageView profilePicture;
        TextView nameSurname;
        TextView lastMessage;
        TextView lastEmotion;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            //profilePicture = itemView.findViewById(R.id.iv_patient);
            nameSurname = itemView.findViewById(R.id.tv_name);
            lastMessage = itemView.findViewById(R.id.tv_last_time_message);
            lastEmotion = itemView.findViewById(R.id.tv_emotion_detected);

        }
    }
}
