import { StyleSheet} from 'react-native';


export const gstyles = StyleSheet.create({
    title_day: {
        fontSize: 20,
        flex: 1,
        margin: 0,
        fontFamily: 'robo',
        textAlign: 'center',
    },
    container: {
        flex: 1,
        backgroundColor: '#B3E2E6',
        padding: '10%',
        alignItems: 'center',
        paddingTop: '15%',
    },
    week:{
        paddingLeft: '5%',
        paddingRight: '15%',
        width: '100%',
        alignItems: 'center',
        justifyContent: "space-evenly",
        backgroundColor: '#7777',
        flexDirection: "row",
        borderRadius: 100,
    },
    selector:{
        flex: 1,
        backgroundColor: '#ccc8',
        height: '100%',
        width: '12.5%',
        borderRadius: 100,
        position: 'relative',
        left: '826%',
    },
    logo:{
        alignSelf: 'center',
        width: 200,
        height: 200,
        marginBottom: '10%',
    },
    button:{
        color: 'green',
        marginHorizontal: '15%',
        width: '70%',
        borderRadius: 5,
        borderWidth: 1,
        borderColor: "#95BFB8",
    },
    input:{
        borderWidth: 1,
        borderRadius: 30,
        borderColor: 'black',
        padding: 10,
        marginVertical: 15,
        marginHorizontal: '20%',
        width: '60%',
    },
    reg: {
        marginTop: '5%',
        alignSelf: 'center',

    },
    day: {
        borderRadius: 40,
        backgroundColor: "#dddddd",
        marginVertical: 15,
        marginHorizontal: 10,
        width: "100%",
        height: "90%",
    },
    important_plan: {
      borderRadius: 10,
      backgroundColor: "#A388FA",
      width: "90%",
      height: 70,
      margin: 10,
      paddingLeft: 10,
      alignItems: "flex-start",
      justifyContent: "center",
    },
    plan: {
        fontFamily: 'robo',
    },
    question: {
        fontFamily: 'robo',
    },
    company_name: {
        fontFamily: 'robo',
        fontSize: 40,
    }
});