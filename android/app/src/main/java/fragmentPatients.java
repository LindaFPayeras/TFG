import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.fragment.app.Fragment;

import com.lily.front.R;

public class fragmentPatients extends Fragment {

    private View view;
    private ReciclerView recyclerView = view.findViewById(R.id.patientList);



    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        return inflater.inflate(R.layout.fragment_patients, container, false);
    }

}
