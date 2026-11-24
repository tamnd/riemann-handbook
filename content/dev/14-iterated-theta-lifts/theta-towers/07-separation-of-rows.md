---
title: Separation of rows by real functionals
decls:
  - GlobalTheory.Twist.CoreOntoAssembly.twist_core_surjective_of_local_components
  - GlobalTheory.T.twist_core_surjective
  - UpperTheory.Lit.bessel_separate_of_step_gap
  - UpperTheory.Lit.real_functionals_separate_of_hypothesis
  - UpperTheory.Lit.functionalsSeparate_of_howeUnram_of_siegelWeil
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Separation of rows by real functionals

This section proves that the rows of the grid are separated by real functionals: for each nonzero vector of the first row model there are a functional on the coefficient space and real vectors such that every nonzero eigenvector of the row is detected by a nonvanishing twisted period. The inputs are unramified Howe duality and the Siegel-Weil formula in its convergent range. The result is the first item of the step [the hypotheses are not empty](/step/nonempty-hyps/), and it is an input of the fit of constant functions in Section 8.

We fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/). We first state the two published inputs.

**Theorem 3.7.1 (Unramified Howe duality).** Let $L$ be a complete nonarchimedean field of characteristic zero with a discrete valuation, and let $(U_1, U_2)$ be an unramified local unitary dual pair over $L$, with groups of integral points $U_1(\mathcal O)$ and $U_2(\mathcal O)$. Let $\omega$ be its Weil representation on a space $M$, with the action $\rho$ of the Heisenberg translations. Let $s \in M$ be a nonzero vacuum vector whose translates $\rho(x)s$ span $M$. Then every vector of $M$ fixed by $U_1(\mathcal O)$ lies in the span of the orbit $\omega(1, U_2)s$, and every vector fixed by $U_2(\mathcal O)$ lies in the span of $\omega(U_1, 1)s$.

This is a lemma of the unramified theta correspondence, after R. Howe, *θ-series and invariant theory*, Proc. Sympos. Pure Math. 33, Part 1 (1979), and S. Rallis, *Langlands' functoriality and the Weil representation*, Amer. J. Math. 104 (1982). We have not checked the exact place of the statement in these papers.

**Theorem 3.7.2 (Siegel-Weil formula, convergent range).** Let $A$ and $B$ be Hermitian spaces over the CM extension $E/F$, of ranks $a$ and $b$, with

$$a < b \le 2a, \qquad a + r(B) < b,$$

where $r(B)$ is the Witt index of $B$. Let $\omega$ be a Weil representation of the pair formed by the doubled space $A \oplus (-A)$ and $B$, for a character $\chi_B$. Fix the archimedean data of the Fock model and a Haar measure on $G_B(\mathbb A)$. Then for every Fock vector $f$ the theta integral of $f$ over $G_B(F) \backslash G_B(\mathbb A)$ converges absolutely, and the value at $s_0$ of the Siegel Eisenstein series of the section of $f$ equals the theta integral.

This is the Siegel-Weil formula of A. Weil, *Sur la formule de Siegel dans la théorie des groupes classiques*, Acta Math. 113 (1965), for unitary groups in Weil's range of convergence; see [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula). The condition $a + r(B) < b$ is Weil's condition for absolute convergence.

We also use a real branching estimate. For discrete series of $\mathrm U(n + 1)$ and $\mathrm U(n)$ with interlacing parameters there are a lowest unit vector $v_0$, a translate $v$ of it, a unit vector $w'$ of the smaller representation and $c > 0$ such that the integral over $\mathrm U(n)$ of the matrix coefficient of $v$ against that of $w'$ is $c$ times the projection onto $w'$, together with integrability bounds for the matrix coefficients. This estimate is proved, so it adds no hypothesis.

**Definition 3.7.3 (Separation of rows).** We say that rows are separated by real functionals if the following holds. For all $\varepsilon$ and $C_F \ge 6510$ there is $x_0$ such that for every datum $D$ with size data of exponent $\varepsilon$, $x \ge x_0$, the size conditions of the rows and the tie with the Eisenstein series, every finite group $\Gamma$, family $A$, number field $K_s$ and real datum $R$ whose level character is good and that has the group record, every grid $G$ at the constants $(1, C_F, b)$ with a Weil datum $W$ over $R$, every volume datum $M$ of row type, and every nonzero smooth vector $w$ of the first row model: there are real vectors $\rho$ and a functional $\xi$ on the coefficient space such that for every nonzero $t$ in the trivial eigenspace $E$ of $R$ there are a column vector $\Psi$ and a theta datum $\Phi$ with

$$f_{\Psi, \Phi}\bigl(F_{w, t}\bigr) \neq 0,$$

the integral that defines it being convergent. Here $F_{w, t}$ is the row form of $w$ and $t$, and $f_{\Psi, \Phi}(F) = B^+(\langle \xi, \Psi \rangle, \theta_\chi(\Phi)(F))$ is the twisted period of the pairing of $\xi$ with $\Psi$ against the twisted theta function.

If $\xi = 0$ the period vanishes, so the separation forces $E = 0$ unless $\xi \neq 0$. We have not unfolded the size data, the tie, the group record or the row form.

**Definition 3.7.4 (Row tower).** The row tower condition says the following, for each datum with the gap condition and each grid $G$ with Weil datum $W$ and volume datum $M$. For every discrete series model $M_0$ at the node $(0, 0)$ with the real data of $W$, and every $n \le m$, there is a discrete series model $M_n$ at $(n, 0)$ with the parameter of the row and the real data of $W$, and a map $\mathrm{vec}$ on vectors, such that for every admissible map $T$ of $M_0$ and every theta datum $\Phi$ there is an admissible map $T'$ of $M_n$ with this property: the lift of $T(w)$ along the bottom row from $(0, 0)$ to $(n, 0)$ converges, and its part at $n$ is $T'(\mathrm{vec}(\rho, w))$ for all $\rho$ and $w$.

So the lifts along the bottom row carry the multiplicity spaces of discrete series into each other.

**Theorem 3.7.5 (Core lifts are onto).** Assume the local inputs, unramified Howe duality, the Siegel-Weil formula in the convergent range, and the inputs on Harish-Chandra modules, rapid decay of cusp forms, discrete series, Casselman-Wallach globalization, the unitary Weil representation, the Weil-Siegel formula, the doubling local zeta integrals and the unramified doubling for $\mathrm{GL}$. Then the core lifts are onto in the following sense. For every datum prime to the level with the size conditions, every grid at gap constant $1$, every volume datum $v$ on the core column and every discrete series model at core node $0$ with the real data of the grid, each value $y(x)$ of a form $y$ of the multiplicity space at the level of the grid, at a $K$-finite pure tensor $x$, lies in the span of the reachable functions of $v$.

A function $F$ on core node $0$ is reachable if there is a chain $\Psi_0 = F, \Psi_1, \ldots, \Psi_m$ of rapidly decreasing functions with $\Psi_i$ the lift of $\Psi_{i+1}$ down the core column with Schwartz data of the right dependence, and $\Psi_m$ the pairing of a functional with a column value.

Lean: `GlobalTheory.Twist.CoreOntoAssembly.twist_core_surjective_of_local_components` (also `GlobalTheory.T.twist_core_surjective`, a second name).

*Proof.* Five facts give the conclusion. (1) Every composite of $k \le m$ lift steps between core stages is surjective; this uses all the inputs. (2) The common data of the test grid have their properties. (3) Each core node has a lattice datum with valid stages. (4) For each $k \le m$ there is a composite of $k$ lift steps whose values on $K$-finite vectors lie in the span of the functions below level $k$ of the chain; this uses discrete series, Harish-Chandra modules, rapid decay, Casselman-Wallach and the models that the local inputs give. (5) Each form on the top core node is a pairing of a functional with a column value. With (1) and (4), a form at the level of the grid is pulled down the core column step by step, and (5) ends the chain at the top. $\square$

**Theorem 3.7.6 (Separation from the step gap).** Assume the local inputs and the row tower condition. Assume also that the size data imply the gap conditions, that the good rows at the principal level are rows, that the separating family converges, and that rows are weakly separated by real functionals. Then rows are separated by real functionals.

Lean: `UpperTheory.Lit.bessel_separate_of_step_gap`.

*Proof.* Three more facts enter. A positivity statement for Hermitian frames, the Bessel gap, holds. The dual of the coefficient space is a tensor product over the real places of finite-dimensional irreducible representations. Theta lifts to the top of the row separate points, by the local inputs. A general separation lemma for Bessel models then gives the separation of rows from these three facts, the row tower condition and the four assumptions. It strengthens the weak separation to the separation with a single theta datum. $\square$

**Theorem 3.7.7 (Separation from the real inputs).** Assume the local inputs, unramified Howe duality, the Siegel-Weil formula in the convergent range and the real branching estimate. Then rows are separated by real functionals.

Lean: `UpperTheory.Lit.real_functionals_separate_of_hypothesis`.

*Proof.* We check the hypotheses of [Theorem 3.7.6](/entry/bessel-separate-of-step-gap/). The local inputs give models of the separating data and a seesaw pair for the theta data, and with them the separating family extends by the twist. This gives the multiplicity spaces along the first row tower, which is the row tower condition. The separating family converges on the row tower. The size data imply the gap conditions, and the good rows at the principal level are rows. For the weak separation we use three facts: the Bessel periods do not vanish along the ascent of depth, the separating family decays rapidly, and the period of an eigenvector does not vanish. The last uses the real branching estimate, with Harish-Chandra modules, Casselman-Wallach and rapid decay. The core lifts are onto by [Theorem 3.7.5](/entry/twist-core-surjective-of-local-components/); this is where Howe duality and Siegel-Weil enter. $\square$

**Theorem 3.7.8 (Separation of rows).** Assume the local inputs, unramified Howe duality and the Siegel-Weil formula in the convergent range. Then rows are separated by real functionals.

Lean: `UpperTheory.Lit.functionalsSeparate_of_howeUnram_of_siegelWeil`.

*Proof.* This is [Theorem 3.7.7](/entry/real-functionals-separate-of-hypothesis/) applied to the local inputs, Howe duality, the Siegel-Weil formula and the real branching estimate, which is proved. $\square$

**Remark 3.7.9 (Formalization).** Unramified Howe duality is a hypothesis here, but it is proved elsewhere in the library, so it adds nothing. Of the eleven published inputs of the theorem on core lifts, nine are also parts of the local inputs, which are a hypothesis as well; only Howe duality and Siegel-Weil are new there. The local inputs enter that theorem only through the models of fact (4). The words "local components" in its name match nothing in the statement. The Siegel-Weil input asks for $b \le 2a$ in addition to Weil's condition. In [FunctionalsSeparateOfHoweUnramOfSiegelWeil.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FunctionalsSeparateOfHoweUnramOfSiegelWeil.lean#L10) lines 10 to 14 are an empty section with unused variables. We have not opened the lemmas of the proofs above, apart from their statements.
