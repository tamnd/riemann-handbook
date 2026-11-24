---
title: The swap relation on a good tower
decls:
  - SquareStatements.good_tower_antisymmetry
  - SquareStatements.antisymmetry_of_singular_statement
  - SquareStatements.good_tower_antisymmetry_of
  - SquareStatements.tie_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The swap relation on a good tower

This section assembles the results of Sections 6 to 10 and 16 into the swap relation for a good tower. A good tower carries root models of unitary Shimura varieties, and each root model has a height polynomial. The relation says that the defect between this polynomial and the volume times the flag height changes sign under every allowed adjacent swap of the weight. We prove it from seven statements about Hodge components, flags and metrics. Six of them are proved in other chapters. The seventh is the statement on singular metrics, and it is proved in the chapter on the heights of the Hodge lines. The relation is the input of [the full intersection relation of a tower](/entry/full-intersection-tower-i8-relation/).

### Root towers and the relation

Let $\Psi$ be a finite set and $N \geq 1$. Let $R$ be the real polynomial ring in the variables $X_{\tau,i}$ with $\tau \in \Psi$ and $0 \leq i < N$, and let $\delta = \lvert\Psi\rvert \binom{N}{2}$. For a weight $\lambda$ put
$$
\ell_\lambda = -\sum_{\tau, i} \lambda(\tau, i) X_{\tau,i} .
$$
For an adjacent swap $(\tau, a, b)$ let $s\lambda$ be $\lambda$ with the entries $(\tau, a)$ and $(\tau, b)$ exchanged.

A root tower has an integer $j$ with $1 \leq j < N$, a finite nonempty set of components $c$ with volumes $\operatorname{vol}(c)$, and for each level $B$ and each $c$ a root model: an arithmetic variety of dimension $\delta + 1$ in a product of projective spaces, with hermitian lines for the roots. For a system of intersection numbers $I$ the root model gives a linear form $\mathrm{PP}^B_c$ on $R$, the limit of the intersection numbers of its lines, normalized by the degree of the model. Let $h_{\mathrm{Fl}}$ be the flag height of Section 10.

**Definition 10.17.1.** A root tower satisfies the swap relation for $I$ if for all $B \geq 2$, all $c$, every adjacent swap $(\tau, a, b)$ with $b \neq j$ and every weight $\lambda$, the defect
$$
D(\lambda) = \mathrm{PP}^B_c(\ell_\lambda^{\delta + 1}) - \operatorname{vol}(c)\, h_{\mathrm{Fl}}(\ell_\lambda^{\delta + 1})
$$
satisfies $D(s\lambda) = -D(\lambda)$.

Let $E$ be a CM field with a host and a hermitian datum of signature $(p, q)$, so that $N = p + q$. Let $\Psi$ be the CM type and $Y$ a model of the moduli space. A good origin of a root tower over $Y$ ties each root model to a Hodge component of $Y$, with a Hodge tie in the sense of Section 6.

### The seven statements

We name seven statements. Each of them concerns one Hodge component or one realization.

1. Smooth approximation. Let a realization of an analytic system have reference lines that are combinations of hermitian lines $\sigma_r$, with the coefficients that express the steps through the roots, and conjugation invariant step lines. Then there are smooth conjugation invariant lines $x_{t,r}$ with the degrees of $\sigma_r$ that, for small $t > 0$, agree on the points of the variety with the combination of the step lines at $t$ that gives the root $r$.
2. Algebraicity. The realization of analytic flag data over a Hodge base metric is algebraic over the flag model.
3. Hodge-Tate pieces. For a map of Hodge components with the same depth function $R$, the condition that the Hodge-Tate pieces at the primes of $S$ are vector bundles passes from the target to the source.
4. Singular metrics. On a flag model with a Hodge base metric, let $\sigma_r$ be Hodge lines of a total tie with the degrees of the roots. Then at every point over a point off the boundary, the combination of the $\sigma_r$ for the step $a$ has the metric of the base metric at $a$.
5. Base. For every compact generic point $\xi_0$ of $Y$ and every finite set $S$ of primes that contains the primes dividing the discriminant of $E$, there is a Hodge component over $\xi_0$ that is a cover, an arithmetic variety of dimension $\dim Y + 1$, with a normal crossings boundary and $R(\ell) = 4$ for $\ell \in S$.
6. Comparison. Two Hodge ties with the same generic point and the same $R$ on $S$, one of degree $1$ and one of the degree of its flag $F$, have height polynomials and degree polynomials that differ by the factor $\deg F$.
7. Fibre squares. Given the antisymmetry theorem of Section 10, the agreement theorem for positive systems and the inputs, a root tower satisfies the swap relation if for each $B$ and $c$ there are a realization with a flag system at $j$ and a number $m > 0$ such that its height polynomial in weight coordinates and its degree polynomial are $m$ times those of the tie of the tower at $(B, c)$.

### The tie

**Theorem 10.17.2 (Root model with a Hodge tie).** Assume statements 1 to 5, the given statements and the statement on Weil pairings. Let $p, q \geq 1$, let $S$ be a finite set of primes that contains the primes dividing the discriminant of $E$, and let $\xi_0$ be a compact generic point of $Y$. Then there are a root model $M'$, a Hodge tie $t$ on $M'$ with $n = [F : \mathbb{Q}]$ for the coefficient field $F$, a number $d$ and a realization $\mathrm{Re}$ of an analytic system of dimension $d + 1$ such that:

1. $t$ has the generic point of $\xi_0$, $R(\ell) = 4$ for $\ell \in S$, its realization has degree $1$, and its flag has positive degree;
2. the system of $\mathrm{Re}$ and the system of $t$ have the same degree polynomial;
3. $\mathrm{Re}$ carries a flag system at $j = p$;
4. $\mathrm{Re}$ and the realization of $t$ have the same height polynomial for every system of intersection numbers.

Lean: `SquareStatements.tie_of`.

*Proof.* Step 1: the base. Statement 5 gives a Hodge component $\mathfrak{M}$ over $\xi_0$ that is a cover of some degree, with a normal crossings boundary and $R(\ell) = 4$ on $S$. Its Hodge bundles have bases.

Step 2: the flag model and the metric. [The flag model of a Hodge component](/entry/flag-model-exists-of-given/) gives a flag model $M$ over coordinates $y$, a Hodge component over the base of $M$ with a flag tie, and a Hodge component over $y$ with a flag $F$ and degrees for the roots. The theorem on base metrics of Section 6 gives a base metric of dimension $n_0 = \lvert\Psi\rvert p q$ that is Hodge for the tie and conjugation invariant.

Step 3: the dimension. We have
$$
\binom{p + q}{2} = p q + \binom{p}{2} + \binom{q}{2},
$$
by induction on $q$. So $\delta = n_0 + \lvert\Psi\rvert \bigl(\binom{p}{2} + \binom{q}{2}\bigr)$. The CM type is nonempty and $p, q \geq 1$, so $\delta \geq 1$, and we write $\delta = d + 1$. Then $y$ is an arithmetic variety of dimension $d + 2$.

Step 4: the flag system. The theorem of Section 7 gives analytic flag data of dimension $d$ for the base metric, with conjugation invariant step lines, and the data are uniformised at $p$. The flag model is a flag cover of itself of degree $1$, with a covering realization whose lines are the lines of the data. The theorem of Section 16 gives a square system for every allowed adjacent swap. So this realization $\mathrm{Re}$ carries a flag system at $p$.

Step 5: the Hodge lines. The flag $F$ gives Hodge lines $\sigma_r$ with the degrees of the roots. The reference lines of the data at the step $a$ have the degree of the combination of the $\sigma_r$ for $a$. Off the boundary, statement 4 and the formula for the weights of the data give
$$
\log \lVert\cdot\rVert_{\Sigma_a} = \log \lVert\cdot\rVert_{\mathrm{ref}_a} + \varphi_a ,
$$
where $\Sigma_a$ is the combination of the $\sigma_r$ for $a$. Statement 2 makes the realization algebraic. Statement 1 gives smooth lines $x_{t,r}$ with the degrees of $\sigma_r$. Statement 3 gives the vector bundle condition for the Hodge component over $y$. Birationality of $y$ holds for a Hodge component with a flag.

Step 6: the root model. Let $M'$ be the root model on $y$ with the lines $x_{t,r}$, the trivial line as the auxiliary line with multiplicity $1$, and the degree $[F : \mathbb{Q}] \deg F$. Let $t$ be the Hodge tie with the flag $F$, the lines $\sigma_r$ and the realization of the data. Two realizations of one system with the same degree and the same lines have the same height polynomial. The covering realization has degree $1$ and the lines of the data, so part 4 holds. Parts 1 to 3 are Steps 1 to 4. $\square$

### The relation

**Theorem 10.17.3 (Swap relation from seven statements).** Assume statements 1 to 7, the comparison of Hodge metrics, the given statements and the statement on Weil pairings. Let $p, q \geq 1$, let a root tower for the CM type and $N = p + q$ have a good origin over $Y$ with the extra conditions, and let $I$ be a full system of intersection numbers. Then the tower satisfies the swap relation for $I$.

Lean: `SquareStatements.good_tower_antisymmetry_of`.

*Proof.* The CM type is nonempty. The tie theorem gives the tie statement. Combine it with statement 6 as follows. Let $(B, c)$ be a level and a component, and let $\xi_0$ be the generic point of the Hodge component of the good origin at $(B, c)$. The tie theorem gives a root model, a tie $t$ and a realization $\mathrm{Re}$ with a flag system at $p$. The good origin gives a second tie at $(B, c)$, of the degree of its flag, with the same generic point and the same $R$ on $S$. Statement 6 gives that its polynomials are $m = \deg F$ times those of $t$, and $m > 0$. By part 4 of the tie theorem the same holds for $\mathrm{Re}$. This is the hypothesis of statement 7, and $j = p$ by the good origin. Statement 7, with the antisymmetry theorem of Section 10, gives the swap relation. $\square$

**Theorem 10.17.4 (Swap relation from the singular statement).** Assume statement 4. Then the conclusion of the previous theorem holds.

Lean: `SquareStatements.antisymmetry_of_singular_statement`.

*Proof.* Statements 1, 2, 3, 5, 6 and 7 are proved theorems. Statement 2 comes from two lemmas: a realization of degree $1$ with no branch set, whose boundary is cut out by a form, is algebraic over the model, and the boundary of a Hodge component is cut out by a form. Apply the previous theorem. $\square$

**Theorem 10.17.5 (Swap relation on a good tower).** Assume the comparison of Hodge metrics, the given statements and the statement on Weil pairings. Let $p, q \geq 1$, let a root tower for the CM type and $N = p + q$ have a good origin over $Y$ with the extra conditions, and let $I$ be full. Then the tower satisfies the swap relation for $I$.

Lean: `SquareStatements.good_tower_antisymmetry`.

*Proof.* Statement 4 is a theorem: the logs of the combined Hodge lines and of the base metric agree off the boundary, by seven lemmas on the Hodge lines of a total tie. Apply the previous theorem. $\square$

The sign change comes from one place: the antisymmetry theorem of Section 10, applied to a realization with a flag system. The rest of the section transports it from the realization of a Hodge tie to the root models of the tower, and the transport costs only the positive factor $m$.

**Remark 10.17.6 (Formalization).** The four theorems are at `Development/WeilBound/CoreStatements/MultihomogeneousSquares/GoodTowerAntisymmetry.lean:20`, `AntisymmetryOfSingularStatement.lean:13`, `GoodTowerAntisymmetryOf.lean:20` and `ChooseTwoAdd.lean:55` in that folder. The first writes out the body of the proposition `GoodTowerAntisymmetry` (`GoodTowerAntisymmetryOf.lean:13`) instead of using its name. The seven statements are `StX`, `StAlg`, `StHt`, `StSing`, `StBase`, `StCmp` and `AntisymmetryFibreSquares` in `AntisymmetryFibreSquares.lean` (lines 37, 59, 66, 78, 102, 28 and 23), with the tie statement `StTie` at line 113; statement 7 is proved by `antisymmetry_transposition_factor`, and the swap relation is `RootTower.I8`. The step that combines the tie with statement 6 is `sq_of` (`SqOf.lean:13`). The tie theorem takes the inputs and resolution from the given statements by position, `hG.2.2.2.2.2.2.2.2.2.1` and `hG.2.2.2.2.1` (lines 57 and 58), and the same projection appears in `GoodTowerAntisymmetryOf.lean:24`. In Step 4 the flag cover is the flag model over itself, from `flag_cover_degree_one_realisation`, so the lifting lemma of Section 16 is used only in degree $1$. The file `ChooseTwoAdd.lean` is named after its helper `choose_two_add` (line 21). The proof of statement 4 is `HeightCancellation.stSing` in `Development/WeilBound/CoreStatements/JacobiBlockDeterminants/StSing.lean`, which passes its seven lemmas to `Sing.stSing_of` in the order `c0`, `c1`, `c2`, `c5`, `c3w`, `c3o`, `c4`. The statement on Weil pairings is `Out.WeilSt`, and it enters only through statement 5.
