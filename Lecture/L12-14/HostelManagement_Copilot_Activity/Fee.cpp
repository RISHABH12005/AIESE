#include "Fee.h"

// Intentional simple fee-calculation function for testing activity.
double calculateHostelFee(double monthlyFee, int lateDays) {
    double penalty = lateDays * 20.0;
    return monthlyFee + penalty;
}
