FILE* fpAA;
fpAA = fopen("program.bin", "ab");
if (fpAA == NULL) {
    printf("Error! opening file");
    exit(1);
}

struct adminInfo a;

fread(&a, sizeof(struct adminInfo), 1, fpAA);
