#include <zmq.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_PSZ_REQUEST 100
#define MAX_BUFFER_RCVD 1024
#define MAX_BUFFER_IN 100

int main (int argc, char* argv[])
{
    int rc; //return code
    void *context = zmq_ctx_new ();
    void *requester = zmq_socket (context, ZMQ_REQ);
    char pszRequest[MAX_PSZ_REQUEST];

    if (argc != 3){
        fprintf(stderr, "Usage: %s <hostname> <port>\n", argv[0]);
        exit(-1);
    }

    char *hostName = argv[1]; //should be localhost for testing
    int serverPort = atoi(argv[2]); //should be 40931 for testing

    printf ("Connecting to server on port %d...\n", serverPort);
    sprintf(pszRequest, "tcp://%s:%d", hostName, serverPort);

    rc = zmq_connect(requester, pszRequest);

    if(rc == 0){
        printf("Successfully connected on port %d\n", serverPort);
    }
    else {
        printf("Network connection failed\n");
        exit(1);
    }

    char buffer[MAX_BUFFER_RCVD];
    char input[MAX_BUFFER_IN];

    while (1){
        fgets(input, MAX_BUFFER_IN, stdin);
        input[strlen(input) - 1] = '\0';

        if (strcmp(input, "exit") == 0){
            printf("Exiting...\n");
            break;
        }

        zmq_send (requester, input, strlen(input), 0);
        memset(buffer, 0, MAX_BUFFER_RCVD);
        zmq_recv (requester, buffer, MAX_BUFFER_RCVD - 1, 0); 
        printf("Received: %s\n", buffer); //print message that was recieved
    }
    
    zmq_close(requester);
    zmq_ctx_destroy(context);

    return 0;
}
