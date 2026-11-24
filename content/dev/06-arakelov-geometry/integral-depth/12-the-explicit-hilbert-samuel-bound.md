---
title: The explicit Hilbert-Samuel bound
decls:
  - GlobalTheory.HSShortTop.geoBound_of_abstract
  - GlobalTheory.T.explicit_arithmetic_hilbertSamuel_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The explicit Hilbert-Samuel bound

This section assembles the last three sections into the geometric bound. The geometric bound is the lower bound $\mathrm{HS}_{26}$ for the slope of the top lattice of hermitian data, stated in [the section on the Hilbert-Samuel bound on a component](/entry/geo-bound-of-quoted-prime/). The assembly takes four statements as hypotheses: the quoted theorems, the Bertini theorem over number fields, the height tie and the slope bound. [The arithmetic Hilbert-Samuel bound](/entry/geo-bound-of-quoted-prime/) then proves the last three of them and applies the result.

We use hermitian data $X$ over a number field $F$, the geometric hypotheses at $\Lambda_0$ and the quoted theorems $\mathsf{Q}$ as in that section, [simple sections](/entry/bertini/), [flat structures](/entry/flat-at-of-simple-at/) and [the slope claim](/entry/slope-top-slope-bound/).

**Definition 3.12.1 (Height of hermitian data).** A real number $h$ is a *height* of $X$ if there are $\delta' \in \mathbb{N}$ with $\delta' > 0$ and a Chow form $f$ of degree $\delta'$ of the image ideal of $X$ such that $(D + 1)\delta' h$ is the height of $f$ in degree $\delta'$. The height of a form is defined by the lattice frame $(w, \mathrm{fr})$ of $X$; we do not unfold it.

**Definition 3.12.2 (Height tie).** The *height tie* says: for every number field $F$, every hermitian tuple $T$ over $F$ whose frame is a lattice frame with constant $\Lambda$, every height $h$ of $T$, all $\delta', e \in \mathbb{N}$ with $e \ge 1$, every Chow form $f$ of degree $\delta'$ of the image ideal and every $c \in F$ with $c \ne 0$,
$$\frac{\mathrm{ht}(c f^e)}{(D + 1) e \delta'} = h - \tfrac12 H_{N - 1}, \qquad h - \tfrac12(\log n + 1) \le \frac{\mathrm{ht}(c f^e)}{(D + 1) e \delta'},$$
where $H_{N-1} = 1 + \frac12 + \dots + \frac1{N-1}$.

The height tie compares two normalizations of the height: the one in the definition of a height of $X$ and the one used in the slope bound. Only its second part is used below.

**Definition 3.12.3 (Slope bound statement).** The *slope bound statement* says that the conclusion of [the slope bound for the top lattice](/entry/slope-top-slope-bound/) holds for every hermitian system over every number field: if the hypotheses hold for $S$, $\delta \ge 1$, $f$ is irreducible and homogeneous of degree $\delta$ in each group, $Q \ne 0$, and $S$ is flat at $s$ for $(\delta, f)$ for all $s$ with $Q(s) \ne 0$, then $\dim V_T > 0$ and the slope claim holds with $h = \mathrm{ht}(f)/((D + 1)\delta)$.

We also need one numerical lemma, proved in the development. It turns the slope claim into the Hilbert-Samuel claim.

**Lemma 3.12.4 (From the slope claim to the Hilbert-Samuel claim).** Let $T, D \in \mathbb{N}$ and $n, \Lambda, \beta, \Lambda_0, \Lambda_D, \Lambda_T, \delta, h, h', d, \deg \in \mathbb{R}$. Assume $1 \le D$, $D + 1 \le T$, $1 \le n$, $1 \le \Lambda$, $1 \le \beta$, $1 \le \delta$ and $h - \frac12(\log n + 1) \le h'$. If $\mathrm{SC}(T, D, n, \Lambda, \beta, \Lambda_0, \Lambda_D, \Lambda_T, \delta, h', d, \deg)$ holds, then
$$\mathrm{HS}_{26}(T, D, n, 1, \Lambda, \beta, \Lambda_D, \Lambda_T, \log\Lambda_0, \delta, h, d, \deg).$$

In this chapter the constant $26$ enters through this lemma. Informally, the extra terms of $\mathrm{HS}_{26}$, such as $3(D+1)|h|$ and $\rho$, leave room for the shift from $h'$ to $h$ and for the terms in $c(n, \Lambda)$ and $\log \beta$ of the slope claim.

**Theorem 3.12.5 (Explicit arithmetic Hilbert-Samuel bound).** Assume the quoted theorems, the Bertini statement over number fields, the height tie and the slope bound statement. Then the geometric bound holds: for every number field $F$, all hermitian data $X$ over $F$, every $\Lambda_0$ such that the geometric hypotheses hold for $X$ at $\Lambda_0$, and every height $h$ of $X$,
$$\mathrm{HS}_{26}(T, D, n, 1, \Lambda, \beta, \Lambda_D, \Lambda_T, \log \Lambda_0, \delta, h, d, \deg M_T).$$

Lean: `GlobalTheory.HSShortTop.geoBound_of_abstract` (also `GlobalTheory.T.explicit_arithmetic_hilbertSamuel_bound`, a second name).

*Proof.* Fix $F$, $X$, $\Lambda_0$ and a height $h$. By the definition of a height there are $\delta' > 0$ and a Chow form $f$ of degree $\delta'$ of the image ideal that realize $h$.

*Bertini.* The tuple of $X$ is geometric, and it is birational by the geometric hypotheses. The Bertini statement over number fields gives $\delta' = \delta$, the self-intersection number of $X$, and a polynomial $Q \ne 0$ such that every $s$ over a number field $E \supset F$ with $Q(s) \ne 0$ is simple for $(X, \delta', f)$.

*The hermitian system.* An input lemma shows that the hypotheses of a hermitian system hold for $S_X$ when the geometric hypotheses hold for $X$ at $\Lambda_0$.

*Flatness.* [The filtration at good sections](/entry/flat-at-of-simple-at/), which uses $\mathsf{Q}$, shows that $S_X$ is flat at $s$ for $(\delta', f)$ for every $s \in F^{D \times N}$ with $Q(s) \ne 0$.

*Irreducibility.* The image ideal is prime, and an input lemma on Chow forms shows that $f$ is irreducible. A Chow form of degree $\delta'$ is homogeneous of degree $\delta'$ in each group.

*The slope bound.* The slope bound statement, applied to $S_X$, $\delta'$, $f$ and $Q$, gives $\dim V_T > 0$ and the slope claim
$$\mathrm{SC}\bigl(T, D, n, \Lambda, \beta, \Lambda_0, \Lambda_D, \Lambda_T, \delta', h', \dim V_T, \deg M_T(S_X)\bigr)$$
with $h' = \mathrm{ht}(f)/((D + 1)\delta')$.

*The numbers of $X$.* The top space $V_T$ of $S_X$ is the image of the space of sections of weight $T$ of $X$ under an injective map, so $\dim V_T = d$. The lattice and the norms of $S_X$ in weight $T$ are the transport of those of $X$ along this isomorphism, and an input lemma on degrees shows that the arithmetic degree does not change under such a transport. So $\deg M_T(S_X) = \deg M_T$.

*The height.* The height tie with $e = 1$ and $c = 1$ gives $h - \frac12(\log n + 1) \le h'$.

*Conclusion.* We have $1 \le D$ and $D + 1 \le T$ from the hypotheses of $S_X$, $1 \le n$ from the data, $1 \le \Lambda$ from the lattice frame, $1 \le \beta$ from the hypotheses, and $1 \le \delta'$. The lemma above turns the slope claim into $\mathrm{HS}_{26}$ with $h$ in place of $h'$. Since $\delta' = \delta$, this is the geometric bound. $\square$

The proof shows where each input enters. The Bertini theorem gives the hypersurface $Q$, the quoted theorems give the filtration at the points off $Q$, the slope bound gives the inequality for the normalized height $h'$ of $f$, and the height tie compares $h'$ with the height $h$ of $X$.

**Remark 3.12.6 (Formalization).** In this proof the quoted theorems are used only to call the filtration at good sections; the Bertini statement enters through the hypothesis, and it uses $\mathsf{Q}$ again only when it is proved ([ExplicitArithmeticHilbertSamuelBound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExplicitArithmeticHilbertSamuelBound.lean#L23)). Only the second part of the height tie is used. The height of $X$ is defined with the height of $f$ in degree $\delta'$, and the slope bound uses the height in degree $0$; the height tie is what links the two, and we have not unfolded either ([IsHeightIffOfDegreeEq.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsHeightIffOfDegreeEq.lean#L189)). The numerical lemma is a wrapper of a lemma in the development that we did not open. The second name is a wrapper.
