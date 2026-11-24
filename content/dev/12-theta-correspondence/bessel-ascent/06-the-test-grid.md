---
title: The test grid
decls:
  - GlobalTheory.GridJoin.exists_gridPre
  - GlobalTheory.GridJoin.exists_gridPre_of_sizes
  - GlobalTheory.GridJoin.exists_gridPre_agree
  - GlobalTheory.T.exists_testGrid_arrows_vacua_intertwiners
  - GlobalTheory.GridJoin.exists_arrows
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The test grid

The ascent moves a nonzero period along a grid of Hermitian spaces. Each arrow of the grid is a theta correspondence with a fixed Weil representation, a vacuum vector and a real intertwiner. This section proves that such a grid of test data exists and matches a given Weil family. The theorem is used for the cusp transitions along the arrows of the grid, and through them for the step [the nonempty hypotheses](/step/nonempty-hyps/). For the background see [theta towers](/learn/theta/#theta-towers) and [seesaw pairs](/learn/theta/#seesaw-pairs).

### Grids and Weil families

Let $m$ be the number of rows of the record $R$. A *grid of spaces* for $R$ is a family of Hermitian spaces over $E$ at the nodes of three kinds:

1. the *vertices* $V_{i,j}$ for $0 \le i, j \le m$;
2. the *core nodes* $P_i$ for $0 \le i \le m$;
3. the *top nodes* $X_j$ for $0 \le j \le m$.

Each space carries a discrete series model at the real places, and the grid carries an idempotent $e \in \mathbb{A}_E$, Hecke characters $\chi_k$ and orthogonal extension data that embed $P_0$, $P_i$ and $X_j$ in the neighbouring vertices.

**Definition 8.6.1 (Arrow).** Let $V$ and $V'$ be nodes of a grid, and let $\chi, \chi'$ be characters. An *arrow* from $V$ to $V'$ is a triple $(\omega, f, I)$ in which $\omega$ is a Weil representation of $U(V)(\mathbb{A}) \times U(V')(\mathbb{A})$ with the splitting characters $\chi, \chi'$, $f$ is a vacuum vector of $\omega$, and $I$ is a linear map from the pluriharmonic polynomials of the pair to the linear maps between the smooth vectors of the two discrete series models. The arrow is *valid* if $\omega$ is a Weil representation for these characters, $f$ is a theta vacuum, and $I$ is a nonzero intertwiner of the real actions.

A *grid of test data* is a grid of spaces together with:

1. a *vertical arrow* from $V_{i+1,j}$ to $V_{i,j}$ for $i < m$ and $j \le m$;
2. for each type $t$ of the record, a *row arrow* from $V_{i,j}$ to $V_{i,j+1}$ for $i \le m$ and $j < m$;
3. for each type $t$, a *column arrow* from $X_j$ to $X_{j+1}$ for $j < m$;
4. a *down arrow* from $P_{i+1}$ to $P_i$ for $i < m$, with an adjoint intertwiner;
5. for each coset $c$ of the level at row $0$, a coset vector $v_{i,c}$ on the symplectic space of $V_{i+1,0}$ and $V_{i,0}$;
6. measures on the groups of the nodes.

The vertical and down arrows use the characters $\chi_{m-i}$ at the ranks of their ends. The row and column arrows use the characters $\mu_{t, j+1}$ of the level datum of $R$. The grid is *valid* if its spaces and characters are as $R$ requires, each arrow is valid, the down intertwiners are adjoint to the up intertwiners, the measures are the principal measures of the levels, and each $v_{i,c}$ is a coset vector for the vacuum of the vertical arrow at $(i, 0)$.

A *Weil family* over $R$ for a second grid $G'$ consists of Weil representations, vacua, orthonormal bases, Cartan data and coset vectors at the nodes and arrows of $G'$. A grid of test data $G$ *matches* a Weil family $W$ if the spaces and characters of $G$ agree with those of $W$ node by node, and the Weil representations, vacua and coset vectors of the arrows of $G$ agree with those of $W$.

### The arrows

**Theorem 8.6.2 (The arrows of a test grid exist).** Assume the published results on discrete series covers and on Harish-Chandra modules, the host hypotheses and the size bounds. Let $R$ be a core record for a face, let the gap constant of the scale be $1$, and let $W$ be a Weil family over $R$ for a grid $G'$. Let $G$ be a grid of spaces whose spaces and characters are valid and agree with $W$. Assume that for each $i < m$ and each coset $\kappa$ of $G'$ at row $i$, the coset vector of $W$ at $\kappa$ is a theta vector at the level, for the vacuum of $W$ at row $i$. Then there are vertical, row, column and down arrows, adjoint intertwiners and coset vectors such that $G$ with these data has valid arrows, valid coset data, and arrows that agree with $W$.

Lean: `GlobalTheory.T.exists_testGrid_arrows_vacua_intertwiners` (also `GlobalTheory.GridJoin.exists_arrows`, the proof).

*Proof.* Each kind of arrow is built in three steps: a Weil representation that agrees with the one of $W$, a theta vacuum, and a nonzero real intertwiner for that representation and vacuum.

1. For the vertical arrows, the Weil representation comes from the agreement with $W$, and the vacuum at $j = 0$ is the vacuum of $W$. The intertwiner is a nonzero real intertwiner for the grid arrow. This uses the size bounds.
2. For the row arrows with $i \ge 1$, the Weil representations come from the row arrows of $W$, and a common real intertwiner exists for all types $t$. This also uses the size bounds. At row $0$, the row arrows are the chain arrows, with unit vacua.
3. For the column arrows, the Weil representations come from $W$, the vacua are column vacua, and the intertwiner is the column intertwiner.
4. For the down arrows, the intertwiner comes with its adjoint.
5. The coset vectors are the coset vectors of $W$, re-indexed by the cosets of the grid.

Outside the ranges of $i$ and $j$, the arrows are filled with the trivial representation, the zero vacuum and the zero map. These values are never used. The clauses of validity and agreement are then read off from the steps. $\square$

### The full grid

Let $q_0$ be the auxiliary split prime of the theta chain and let $g_0$ be the first type prime of the host.

**Theorem 8.6.3 (A grid that agrees with an ordered Weil family).** Assume the published results on the existence of discrete series of $U(p, q)$, on discrete series covers and on Harish-Chandra modules, the host hypotheses, the size bounds and $q_0 < g_0$. Let $R$ be a core record for a face, let the gap constant be $1$, and let $W$ be a Weil family over $R$ for a grid $G'$. Assume:

1. the lattice of $G'$ at each node in range off row $0$ is the standard lattice of its space;
2. at each vertex $V_{i,j}$ with $1 \le i$, at each core node and at each top node $X_j$ with $1 \le j$, and at each real place $\tau$, the orthonormal basis $b$ of $W$ satisfies $b^* \,\mathrm{Gram}\, b = J_\varepsilon$ for signs $\varepsilon$ that enumerate the local parameter of the node;
3. the Cartan data and the orthonormal bases of $W$ at $X_0$ and at $P_m$ are equal.

Then there is a valid grid of test data $G$ that agrees with $W$.

Lean: `GlobalTheory.GridJoin.exists_gridPre_agree`.

*Proof.* The coset vectors of $W$ are theta vectors at the level. A grid of spaces with valid spaces and characters that agree with $W$ comes from the level choice grid. This uses three facts about $q_0$: the core places are injective under restriction, the auxiliary prime splits completely, and $q_0$ is not a type prime and not a level prime. The last fact follows from $q_0 < g_0$. The previous theorem gives the arrows. Measures exist on any grid of valid spaces, and adding arrows and measures keeps validity and agreement. $\square$

**Theorem 8.6.4 (A grid that matches a Weil family, under the size bounds).** Assume the published results on the existence of discrete series of $U(p, q)$, on discrete series covers and on Harish-Chandra modules, the host hypotheses, the size bounds and $q_0 < g_0$. Let $R$ be a core record for a face, let the gap constant be $1$, and let $W$ be a Weil family over $R$. Then there is a valid grid of test data that matches $W$.

Lean: `GlobalTheory.GridJoin.exists_gridPre_of_sizes`.

*Proof.* First replace $W$ by a Weil family with the same data whose lattices off row $0$ are standard. Then permute the columns of the orthonormal bases at each node off row $0$ and at each real place, so that $b^* \,\mathrm{Gram}\, b = J_\varepsilon$ with signs that enumerate the local parameters. At row $0$ the bases do not change. The previous theorem gives a valid grid that agrees with the new family. Agreement with the new family gives a match with $W$, since the bases differ only by a permutation of columns off row $0$ and are equal at row $0$. $\square$

**Theorem 8.6.5 (A grid that matches a Weil family).** Assume the published results on the existence of discrete series of $U(p, q)$, on discrete series covers and on Harish-Chandra modules, and the host hypotheses. Let the size data satisfy the size rows. Let $R$ be a core record for a face, let the gap constant be $1$, and let $W$ be a Weil family over $R$. Then there is a valid grid of test data that matches $W$.

Lean: `GlobalTheory.GridJoin.exists_gridPre`.

*Proof.* The size rows give the size bounds. They also give $\log q_0 \le L$ for the scale $L$, so $q_0 \le b$ for the scale constant $b = e^{L}$, and a lower bound for $g_0$ in terms of $(kb)^8$ with $k \ge 2$. Since $kb \le (kb)^8$, this gives $q_0 < g_0$. This is the previous theorem applied to these two facts. $\square$

**Remark 8.6.6 (Formalization).** The four theorems are in [AuxiliaryPrimeLtFirstTypePrimeOfSizes.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/AuxiliaryPrimeLtFirstTypePrimeOfSizes.lean#L123), a file named after the helper that proves $q_0 < g_0$. That helper reads the size rows by long chains of projections, such as a chain of twenty-three projections at line 114. The call of the arrow theorem at lines 145 to 147 tries two forms, with and without the size bounds. The hypothesis $q_0 < g_0$ is used only to show that $q_0$ is not a level prime. We have not unfolded the size rows, the size bounds, the host hypotheses, the core condition, the enumeration of local parameters, the orthogonal extension data or the definitions of a coset vector and of a principal measure.
