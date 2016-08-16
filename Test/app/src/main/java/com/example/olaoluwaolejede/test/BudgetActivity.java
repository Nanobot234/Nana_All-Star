package com.example.olaoluwaolejede.test;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;


public class BudgetActivity extends AppCompatActivity {
    EditText numTxt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_budget);


        String name = getIntent().getExtras().getString("name");
        TextView nView = (TextView) findViewById(R.id.nameView);
        nView.setText("Hi, " + name);

        final Button forBtn = (Button) findViewById(R.id.But2);
        forBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick (View view){
            numTxt = (EditText) findViewById(R.id.moneyView);
            String moneyView = numTxt.getText().toString();



                Intent intent = new Intent(BudgetActivity.this, FoodPlaceActivity.class);

                Bundle bundle = new Bundle();
                bundle.putString("money",moneyView);
                intent.putExtras(bundle);
                BudgetActivity.this.startActivity(intent);




            }

        });

    }
}









