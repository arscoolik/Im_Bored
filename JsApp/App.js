import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import { StyleSheet, Text, View,} from 'react-native';
import Main from './components/main'
import Survey from './components/survey'
import Start from './components/start'
import Reg from './components/reg'
import * as Font from 'expo-font';
import AppLoading from 'expo-app-loading';

const fonts = () => Font.loadAsync({
  'robo_it': require('./fonts/Robo_It.ttf'),
  'robo': require('./fonts/Robo.ttf'),
});

export default function App() {
  const [font, setFont] = useState(false);

  if (font) {
    return (
        <Main/>
    );
  }
  else{
    return(
      <AppLoading startAsync={fonts}
                  onFinish={()=>setFont(true)}
                  onError={console.warn}/>
    );
  }
}

