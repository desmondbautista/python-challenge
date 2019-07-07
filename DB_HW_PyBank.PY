{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Desmond Bautista\n",
    "# Code for pyBank Assignment\n",
    "\n",
    "import os\n",
    "import csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set path for file\n",
    "csvpath = 'FreshShell/Learnpython/Budget_data.csv'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set variables\n",
    "total_months = 0\n",
    "total_profit_loss = 0\n",
    "prev_profit_loss = 0\n",
    "month_change = 0\n",
    "total_month_change = 0\n",
    "average_month_change = 0\n",
    "greatest_increase = 0\n",
    "greatest_increase_month = \"\"\n",
    "greatest_decrease = 0\n",
    "greatest_increase_month = \"\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'FreshShell/Learnpython/Budget_data.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-26-ccce0723fc17>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Open the CSV\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcsvpath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnewline\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mcsvfile\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m     \u001b[0mcsvreader\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcsv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcsvfile\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdelimiter\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\",\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;31m# Code to read the header first\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'FreshShell/Learnpython/Budget_data.csv'"
     ]
    }
   ],
   "source": [
    "# Open the CSV\n",
    "with open(csvpath, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    # Code to read the header first\n",
    "    csv_header = next(csvreader)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'csvreader' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-4ea413c70cf1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Read each row of data after the header\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mrow\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mcsvreader\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m     \u001b[0;31m# count the total number of months\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mtotal_months\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'csvreader' is not defined"
     ]
    }
   ],
   "source": [
    " # Read each row of data after the header\n",
    "for row in csvreader:\n",
    "        # count the total number of months\n",
    "        total_months += 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'row' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-7-2841027e0f75>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# add up the total NET profit/loss\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mtotal_profit_loss\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'row' is not defined"
     ]
    }
   ],
   "source": [
    "# add up the total NET profit/loss\n",
    "total_profit_loss += int(row[1])\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate the change in profit/loss between months\n",
    "if total_months > 1:\n",
    "    month_change = int(row[1]) - prev_profit_loss\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# add up the total monthly change\n",
    "    total_month_change += month_change\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# profit/loss value for previous month\n",
    "    prev_profit_loss = int(row[1])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate greatest increase in profits\n",
    "    if month_change > greatest_increase:\n",
    "            greatest_increase = month_change\n",
    "            greatest_increase_month = row[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate greatest decrease in losses\n",
    "    if month_change < greatest_decrease:\n",
    "            greatest_decrease = month_change\n",
    "            greatest_decrease_month = row[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate average change between months        \n",
    "average_month_change = total_month_change / (total_months - 1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the analysis to terminal\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------\")        \n",
    "print(\"Total Months: \" + str(total_months))\n",
    "print(\"Total: $\" + str(total_profit_loss))\n",
    "print(\"Average Change: $\" + str(format(average_month_change, '.2f')))\n",
    "print(\"Greatest Increase in Profits: \" + greatest_increase_month \n",
    "      + \" ($\" + str(greatest_increase) + \")\")\n",
    "print(\"Greatest Decrease in Profits: \" + greatest_decrease_month \n",
    "      + \" ($\" + str(greatest_decrease) + \")\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write to text file\n",
    "f = open(\"analysis.txt\", \"w\")\n",
    "f.write(\"Financial Analysis\\n\")\n",
    "f.write(\"----------------------------\\n\")        \n",
    "f.write(\"Total Months: \" + str(total_months) + \"\\n\")\n",
    "f.write(\"Total: $\" + str(total_profit_loss) + \"\\n\")\n",
    "f.write(\"Average Change: $\" + str(format(average_month_change, '.2f')) + \"\\n\")\n",
    "f.write(\"Greatest Increase in Profits: \" + greatest_increase_month \n",
    "      + \" ($\" + str(greatest_increase) + \")\\n\")\n",
    "f.write(\"Greatest Decrease in Profits: \" + greatest_decrease_month \n",
    "      + \" ($\" + str(greatest_decrease) + \")\\n\")\n",
    "f.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:FreshShell] *",
   "language": "python",
   "name": "conda-env-FreshShell-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
