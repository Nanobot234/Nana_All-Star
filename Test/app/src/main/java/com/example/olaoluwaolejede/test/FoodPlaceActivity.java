package com.example.olaoluwaolejede.test;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;

public class FoodPlaceActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_food_place);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);


        String value = getIntent().getExtras().getString("money");

        int budget = parseWithDefault(value,0);
        TextView txtView = (TextView) findViewById(R.id.textView11);
        txtView.setText("Your budget is, $" + budget);


        final Button ResBtn = (Button) findViewById(R.id.But3);
        ResBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //contBtn.setText("Clicked");
                Intent intent = new Intent(FoodPlaceActivity.this, RestaurantsPageActivity.class);
                FoodPlaceActivity.this.startActivity(intent);


            }

        });
    }

    public int parseWithDefault(String num, int zero){
        try{
            return Integer.parseInt(num);

        }catch(NumberFormatException e){
            return zero;
        }
    }
}
