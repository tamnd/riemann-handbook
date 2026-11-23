---
title: The green window
decls:
  - UpperTheory.Top.zero_free_all_of_green_v_win
  - UpperTheory.Top.every_character_of_green_v_win
  - UpperTheory.LiteratureTheorems.siegel_weil_std_of_literature
  - UpperTheory.LiteratureTheorems.theta_integrals_agree_and_local_matching_of_literature
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The green window

This section joins the results of the chapter. From Green, the window bound VWin and a record HypsAlt, it proves that no Dirichlet $L$-function vanishes in $\operatorname{Re} s > \tfrac12$. This is the [[Generalized Riemann hypothesis|DNKA4WBKDS]] for Dirichlet $L$-functions, in the form [EveryCharacter](/step/every-character-def/). The two theorems are the steps [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/) and [EveryCharacter from Green, VWin and HypsAlt](/step/green-vwin/). The section then proves two theta inputs of the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/), which applies the second theorem.

We keep the notation of the earlier sections: the shape implication $\mathrm{Shape}(N)$, the slot $N(\mathcal{C}) = \mathrm{Closed}(\mathcal{C}, \mathrm{Link}_N)$, the statement $\mathrm{Top}_G$, and the requirement $G_\psi$.

**Definition 3.7.1 (The record HypsAlt).** $\mathrm{HypsAlt}(N, R)$ is the record of 46 fields of [the record HypsAlt](/step/hyps-alt-def/), with the slot $N$ and the definite side condition $R$ of [the definite side condition](/step/definite-side-condition-def/). A value holds a family class $\mathcal{A}$, a selection, constants and bounds; the shape form reads its fields as its hypotheses.

**Theorem 3.7.2 (ZeroFreeAll from Green, VWin and HypsAlt).** Assume Green, VWin, and that $\mathrm{HypsAlt}(N, R)$ has a value. Then $L(s, \psi) \neq 0$ for each primitive [[Dirichlet character|JR4QSEFXWF]] $\psi$ and each $s$ with $\operatorname{Re} s > \tfrac12$.

Lean: `UpperTheory.Top.zero_free_all_of_green_v_win`

*Proof.* Take a value of the record. [The shape theorem](/entry/shape-closed-link-n-of-green/) gives $\mathrm{Shape}(N)$ from Green. A proved lemma feeds the fields of the record into the hypotheses of the shape form, with the two slots that are $\mathrm{True}$ filled trivially, and gives $\mathrm{Top}_G$. [The hosts for one character](/entry/supply-chi/) give, for each primitive $\psi$, hosts with $G_\psi.\mathrm{req}$ on windows of scale $\tfrac32$, from $\mathrm{VWin}(\psi, 401)$. Then [ZeroFreeAll from $\mathrm{Top}_G$ and hosts](/entry/zero-free-all-of-top-g/) with $\lambda = \tfrac32$ gives the claim. $\square$

**Theorem 3.7.3 (EveryCharacter from Green, VWin and HypsAlt).** Assume Green, VWin, and that $\mathrm{HypsAlt}(N, R)$ has a value. Let $N_0 \ge 1$, let $\chi$ be a Dirichlet character modulo $N_0$, and let $s \in \mathbb{C}$ with $\operatorname{Re} s > \tfrac12$ and with $\chi \neq 1$ or $s \neq 1$. Then $L(s, \chi) \neq 0$.

Lean: `UpperTheory.Top.every_character_of_green_v_win`

*Proof.* This is [the step from primitive to all characters](/step/imprimitive/) applied to [ZeroFreeAll from Green, VWin and HypsAlt](/entry/zero-free-all-of-green-v-win/). The [[Euler product|0C3PN4075R]] relation $L(s, \chi) = L(s, \chi^*) \prod_{p \mid N_0} (1 - \chi^*(p) p^{-s})$, with $\chi^*$ the primitive character that induces $\chi$, has no zero factor for $\operatorname{Re} s > 0$. $\square$

The step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/) applies the last theorem. Its seven inputs give Green and a value of the record. Two of them are statements on theta integrals of [[unitary groups|0R9R0Y1HDK]], and the rest of the section proves them. See [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula) and [the doubling method](/learn/theta/#the-doubling-method) in Volume 1.

**Definition 3.7.4 (The standard Siegel-Weil statement).** Let $F$ be a number field and $E$ a number field over $F$ with an $F$-automorphism $\sigma$, and let $B$ be a good base. Let $m, n \ge 1$, and let $A$ and $Y$ be spaces of dimensions $m$ and $n$ with signatures $(r, s)$ and $(r', s')$, with $\min(r, s) = 0$, one Hermitian and the other skew-Hermitian. Let $\chi$ be a Hecke character with the residue condition at the power $m$. Let a doubling datum be given with the [[Weil representation|H3Q2703KKV]] $\omega$, a map $S$ and a functional $l$. Let $b$ be a frame of $Y$, $K$ a standard compact subgroup and $a$ a height. Let $\mu$ be a Haar measure on the adelic unitary group of $A$ and $D$ a fundamental domain of the rational points. *SiegelWeilStd* says: for each Schwartz function $\Phi$ whose translates under $K$ span a finite-dimensional space, the value at $s_0 = (m - n)/2$ of the [[Eisenstein series|3NZBZXYWAJ]] of the section $x \mapsto l(\omega(x)\Phi)$ equals

$$\kappa \cdot \frac{1}{\mu(D)} \int_D \theta\bigl(\omega(x) S(g) \Phi\bigr)\, d\mu(g), \qquad \kappa = \begin{cases} 1 & n < m, \\ 2 & n \ge m. \end{cases}$$

**Theorem 3.7.5 (The standard Siegel-Weil formula).** Let $O$ be a proof of the open literature statements. Then SiegelWeilStd holds.

Lean: `UpperTheory.LiteratureTheorems.siegel_weil_std_of_literature`

*Proof.* This is [the standard Siegel-Weil formula](/entry/siegel-weil-std/) of Volume 12, which is proved outright; $O$ is not used. $\square$

**Definition 3.7.6 (Theta inputs).** *EisBL* says: for the data above with one space $Y$ and a section $f$ of the induced representation, the Eisenstein series converges for $\operatorname{Re} s > t$ for some $t$ and is holomorphic there; and at each $s_0$ there is $k$ such that $(s - s_0)^k$ times the series is holomorphic near $s_0$ as a functional on forms of moderate growth. *LocalMatching* says: for each admissible triple of a unitary dual pair over a CM extension, at each place the two local Weil representations have matched quotient maps onto one irreducible representation of $U_W$. *ThetaIntegralsAgree* says: for each admissible triple, the global theta integrals decay; when the test data match, the two theta integrals into $U_W$ are proportional with one nonzero constant, and a coinvariance law holds; and two recursion laws relate the constants for sizes $b + 2$ and $b$ by a factor with a partial Hecke $L$-value.

**Theorem 3.7.7 (Theta integrals agree and local matching).** Let $O$ be a proof of the open literature statements. Then ThetaIntegralsAgree and LocalMatching hold.

Lean: `UpperTheory.LiteratureTheorems.theta_integrals_agree_and_local_matching_of_literature`

*Proof.* [Theorem K at the second head](/entry/theorem-k-head2/) of Volume 12 says that EisBL and SiegelWeilStd imply ThetaIntegralsAgree and LocalMatching. EisBL is a proved theorem on Eisenstein series, and SiegelWeilStd is [the standard Siegel-Weil formula](/entry/siegel-weil-std-of-literature/). $\square$

**Remark 3.7.8 (Formalization).** The first two theorems are in TopPlug.lean (lines 12 and 16), which sets `synthInstance.maxHeartbeats 200000` at line 8. The two `True` slots of the shape form are filled with `trivial trivial`. The last two are in [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacterOfLiteratureOfVWin.lean#L563) at lines 563 and 565. Both take the structure `OpenLiteratureStatements` as `O` and never read it: `siegel_weil_std_of_literature O` is the closed term `siegelWeilStd`, and `eis_bl_of_literature O` is the closed term `eisBL`. So the names "of literature" hide two outright proofs. The scale $\lambda = \tfrac32$ is fixed in `zero_free_all_of_green_v_win`, and VWin enters only through `supplyChi`. We have not unfolded the doubling datum `IsDbl`, the residue condition `ResEtaPow` or the frame and height conditions.

## Notes and references

The chapter feeds the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/), and through it [EveryCharacter from the literature and VWin](/step/every-character-of-literature/) and [the literature chapter](/proof/literature/). Its analytic half, the Chebyshev bound and the window criterion of Sections 1 and 2, turns bounds on windows $[Y, Y^\lambda]$ into zero-free half-planes. Its arithmetic half, the hosts of Section 3, uses [VWin](/proof/vwin/). The local and division bounds of Sections 4 to 6 come from the [theta matching chapter](/proof/theta-matching/) and the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

- H. Davenport, *Multiplicative Number Theory*, Chapters 5, 14, 19 and 21, for primitive characters, the zero-free region, the explicit formula and the Siegel exceptional zero.
- H. Iwaniec and E. Kowalski, *Analytic Number Theory*, Chapters 5 and 18, for the explicit formula, Landau type criteria and the least prime in a progression.
- U. V. Linnik, "On the least prime in an arithmetic progression", Mat. Sb. 15 (1944), for the statement SmallOne.
- D. A. Cox, *Primes of the Form $x^2 + ny^2$*, Section 7, for primes represented by norm forms.
- W. Fulton and J. Harris, *Representation Theory*, Lecture 6, for the Weyl dimension formula, the branching rule and the Pieri rule for $\mathrm{GL}_n$.
- A. Weil, "Sur certains groupes d'opérateurs unitaires", Acta Math. 111 (1964), for the Weil representation and the Siegel-Weil formula.
- S. S. Kudla and S. Rallis, "A regularized Siegel-Weil formula: the first term identity", Ann. of Math. 140 (1994), and A. Ichino, "A regularized Siegel-Weil formula for unitary groups", Math. Z. 247 (2004), for the Siegel-Weil formula of unitary dual pairs. The statement ThetaIntegralsAgree is specific to this proof, and no source states it in this form.
