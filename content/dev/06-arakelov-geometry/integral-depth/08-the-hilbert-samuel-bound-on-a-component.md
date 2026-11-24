---
title: The Hilbert-Samuel bound on a component
decls:
  - GlobalTheory.HSShort.geoBound_of_quoted'
  - GlobalTheory.T.arithmeticHilbertSamuelBound
  - GlobalTheory.HSShort.hsClaimS_component_geo
  - GlobalTheory.T.hilbertSamuel_component_short_basis_bound
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Hilbert-Samuel bound on a component

This section states an arithmetic Hilbert-Samuel bound for hermitian data over a number field and applies it to one component of the moduli space. The bound gives a lower bound for the degree of the lattice of sections of high weight in terms of the height and the degree of the image of the component. The general bound is an assembly of three results of the second half of this chapter and one bound on heights. The bound on a component is the input of [the Hilbert-Samuel estimate at a level](/entry/hilbert-samuel-estimate-at-level/) of the previous chapter ([arithmetic volume and bigness](/learn/arakelov/#arithmetic-volume-and-bigness)).

**Definition 3.8.1 (Quoted theorems).** The *quoted theorems* are eight published results that we take as hypotheses: the Kawamata-Viehweg vanishing theorem, the $L^2$ extension theorem for log canonical pairs, the comparison of Serre between holomorphic and algebraic sections, the numerical properties of nef bundles, the existence of Chow forms over a field and over the ring of integers, the behaviour of Chow forms under hyperplane sections, and the length formula for proper intersections. We write $\mathsf{Q}$ for their conjunction.

Hermitian data $X$ over a number field $F$ consist of a projective tuple with an image of dimension $D$, two line bundles $L$ and $L_2$, a length $T$, numbers $n$, $d$ and $\delta$, constants $\Lambda$, $\beta$, $\Lambda_D$, $\Lambda_T$, a multiplication of sections, and for each $j \le T$ an $\mathcal{O}_F$-lattice $M_j$ of sections of weight $j$ with norms at the complex embeddings of $F$ ([hermitian lattices](/learn/hermitian-lattices/#lattices-over-dedekind-domains)). Here $\delta$ is the self-intersection number of the tuple, $d$ is the dimension of the space of weight $T$, and $\deg M_T$ is the arithmetic degree of $M_T$. A real number $h$ is a *height* of $X$ if it is the normalized height of the image, computed from a Chow form ([heights](/learn/arakelov/#heights)). We do not unfold these notions.

**Definition 3.8.2 (Geometric hypotheses).** Let $\Lambda_0 \in \mathbb{R}$. The *geometric hypotheses* hold for $X$ at $\Lambda_0$ if:

1. $F$ is totally complex ([kinds of number fields](/learn/number-fields/#kinds-of-number-fields));
2. the map of the tuple onto its image is birational;
3. $L$ and $L_2$ are nef and big;
4. the multiplication is stable on the lattices, bounded by $\beta$, and the norms are compatible with it;
5. $1 \le \Lambda$ and $1 \le \Lambda_0$;
6. $M_0$, $M_D$ and $M_T$ have bases whose norms are at most $\Lambda_0$, $\Lambda_D$ and $\Lambda_T$.

**Definition 3.8.3 (Hilbert-Samuel claim).** Let $C \in \mathbb{R}$, $T, D \in \mathbb{N}$ and $n$, $j_0$, $\Lambda$, $\beta$, $\Lambda_D$, $\Lambda_T$, $J$, $\delta$, $h$, $d$, $\deg$ real numbers. Put
$$\begin{aligned}
\rho &= \log \Lambda + C \log\bigl(n D j_0 \delta\, (2 + |h| + \log \Lambda)\bigr), \\
G &= \tfrac12 (D + 1)(\log n + 1) + 1, \\
z &= 1 - \tbinom{T - 1}{D} \frac{\delta}{d}.
\end{aligned}$$
Put
$$\begin{aligned}
A &= T h - 3(D + 1)|h| - J - C D^2 (\rho + \log T) \\
&\quad - (T + D + 1) \log \beta - (T + D^2)(G + 2), \\
B &= T \log\bigl(2 e^{\rho} \sqrt{\beta}\bigr) + \log \Lambda_D + \log \Lambda_T.
\end{aligned}$$
The *Hilbert-Samuel claim* $\mathrm{HS}_C(T, D, n, j_0, \Lambda, \beta, \Lambda_D, \Lambda_T, J, \delta, h, d, \deg)$ says that $0 \le z \le 1$ and
$$(1 - z) A - z B \le \frac{\deg}{d}.$$

Informally, $\binom{T - 1}{D}\delta$ estimates the dimension of the deep part of the filtration in weight $T$, so $1 - z$ is its share of the $d$ sections. The term $(1 - z) A$ comes from the deep sections and grows like $T h$, and the term $z B$ is the loss on the other sections, which have small norms.

**Definition 3.8.4 (Geometric bound).** The *geometric bound* holds if for every number field $F$, all hermitian data $X$ over $F$ and all $\Lambda_0$ such that the geometric hypotheses hold for $X$ at $\Lambda_0$, and every height $h$ of $X$,
$$\mathrm{HS}_{26}(T, D, n, 1, \Lambda, \beta, \Lambda_D, \Lambda_T, \log \Lambda_0, \delta, h, d, \deg M_T).$$

**Theorem 3.8.5 (Arithmetic Hilbert-Samuel bound).** If the quoted theorems hold, then the geometric bound holds.

Lean: `GlobalTheory.HSShort.geoBound_of_quoted'` (also `GlobalTheory.T.arithmeticHilbertSamuelBound`, a second name).

*Proof.* [The explicit arithmetic Hilbert-Samuel bound](/entry/explicit-arithmetic-hilbert-samuel-bound/) gives the geometric bound from $\mathsf{Q}$ and three further statements. We supply each of them.

1. *Bertini over number fields.* For a geometric birational tuple and a Chow form $f$ of degree $\delta'$ of its image, $\delta'$ is the self-intersection number, and there is a nonzero polynomial $Q$ such that every linear section $s$ with $Q(s) \ne 0$, over any finite extension, cuts the image in exactly $\delta'$ distinct points, and $f$ at $s$ is a product of linear forms in these points. [The Bertini theorem from the Hilbert-Samuel data](/entry/t-bertini-number-field-of-hilbert-samuel/) proves this from $\mathsf{Q}$.
2. *Height tie.* For a lattice with norms bounded by $\Lambda$, a height $h$ of the tuple, a Chow form $f$ of degree $\delta'$, an integer $e \ge 1$ and $c \in F$, the height of $c f^e$, divided by $(D + 1) e \delta'$, equals $h - \tfrac12 H_{N - 1}$, where $H_{N-1}$ is the harmonic number, and is at least $h - \tfrac12(\log n + 1)$. This follows from a lemma that the height of a product of multihomogeneous polynomials is the sum of the heights and that nonzero constants have height $0$. Both are proved in the development; we do not reproduce them here.
3. *Slope bound.* For a hermitian system that satisfies its hypotheses and an irreducible multihomogeneous $f$ of degree $\delta' \ge 1$ that is flat at every section off a hypersurface $Q = 0$, the top space is nonzero and the claim holds with the height of $f$ divided by $(D + 1)\delta'$. This is [the slope bound for the top lattice off a hypersurface](/entry/slope-lower-bound-top-lattice-off-hypersurface/).

The explicit bound applied to $\mathsf{Q}$ and these three statements gives the geometric bound. $\square$

The theorem is the general step. The rest of the section specializes it. Let $E$ be a CM field with host data $H$, $\mathcal{D}$ a datum, a level and a moduli space with coefficients in $F$, a model $Y$ over $F$, a flag cover of $Y$ and a component $Z$. Fix uniformizations $U$ at level $r$, a rational point $P$ with its length $T$ and weights $P.\mathrm{wt}(j)$ for $j \le T$, a quotient weight $u_1$ of $P$, a dictionary of frames and the other data of a hermitian presentation $h$ of $Z$. A choice $(f_1, f_2, \theta, k)$ of frames and constants gives hermitian data $X = h(f_1, f_2, \theta, k)$ over $F$. Write $\dim \mathcal{D}$ for the dimension of the flag variety of $\mathcal{D}$, and for a weight $w$:

- $\deg_Z(w)$ for the degree of the image of $Z$ for $w$;
- $\mathrm{ht}_Z(w)$ for the height of this image;
- $S_Z(w)$ for the space of cusp forms of weight $w$ on $Z$;
- $\deg_{\mathrm{lat}, Z}(w)$ for the degree of the lattice of integral cusp forms of weight $w$ on $Z$.

Let $w_1$ be the weight of $u_1$ and $w_T = P.\mathrm{wt}(T)$.

**Theorem 3.8.6 (Hilbert-Samuel bound on a component).** Assume the quoted theorems. For all data as above and every $\Lambda_0$ such that the geometric hypotheses hold for $X$ at $\Lambda_0$,
$$\begin{aligned}
\mathrm{HS}_{26}\bigl(&T, \dim \mathcal{D}, n(f_1), 1, \Lambda_k, \beta_k, \Lambda_{D,k}, \Lambda_{T,k}, \log \Lambda_0, \\
&\deg_Z(w_1), \mathrm{ht}_Z(w_1), \dim S_Z(w_T), \deg_{\mathrm{lat}, Z}(w_T)\bigr),
\end{aligned}$$
where $n(f_1)$ is the number of the frame $f_1$ and $\Lambda_k$, $\beta_k$, $\Lambda_{D,k}$, $\Lambda_{T,k}$ are the constants of $k$.

Lean: `GlobalTheory.HSShort.hsClaimS_component_geo` (also `GlobalTheory.T.hilbertSamuel_component_short_basis_bound`, a second name).

*Proof.* We compare the numbers of $X$ with the numbers of $Z$ and then apply the previous theorem.

A lemma on presentations, an input, shows that the dimension $D$ of $X$ is $\dim \mathcal{D}$ and that $Z$ presents the hermitian system of $X$ through the frame $f_1$. With the birationality in the geometric hypotheses, a lemma on image degrees gives $\deg_Z(w_1) = \delta$. With the birationality and the condition that $F$ is totally complex, a lemma on heights of birational images shows that $\mathrm{ht}_Z(w_1)$ is a height of $X$. Both lemmas are inputs that use $\mathsf{Q}$.

The arithmetic Hilbert-Samuel bound, applied to $X$, $\Lambda_0$ and the height $\mathrm{ht}_Z(w_1)$, gives
$$\mathrm{HS}_{26}(T, D, n, 1, \Lambda, \beta, \Lambda_D, \Lambda_T, \log \Lambda_0, \delta, \mathrm{ht}_Z(w_1), d, \deg M_T)$$
for the numbers of $X$. A lemma on lattices of components, an input, gives $\deg M_j = \deg_{\mathrm{lat}, Z}(P.\mathrm{wt}(j))$ for $j \le T$; we use it at $j = T$. The presentation gives $d = \dim S_Z(w_T)$ and identifies $T$, $n$, $\Lambda$, $\beta$, $\Lambda_D$ and $\Lambda_T$ of $X$ with the length of $P$, $n(f_1)$ and the constants of $k$. We substitute these equalities and $\delta = \deg_Z(w_1)$, $D = \dim \mathcal{D}$ in the claim. The result is the stated claim. $\square$

**Remark 3.8.7 (Formalization).** The arithmetic Hilbert-Samuel bound is pure assembly: one term applies the explicit bound to the Bertini theorem, the height tie and the slope bound ([ArithmeticHilbertSamuelBound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithmeticHilbertSamuelBound.lean#L19)). The second name is a wrapper closed by the usual `first | exact @X | exact X | ...` ([ArithHilbertSamuelBoundOfQuotedTheoremsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ArithHilbertSamuelBoundOfQuotedTheoremsStatement.lean#L13)). The height tie is stated with an equality to $h - \tfrac12 H_{N-1}$ and a lower bound by $h - \tfrac12(\log n + 1)$ on the same quantity, so the second part follows from the first only when $H_{N-1} \le \log n + 1$ ([HermSysHypOneLeLambdaZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HermSysHypOneLeLambdaZero.lean#L73)). In the claim, the term $C D^2 \log(e^\rho T)$ is written with an exponential inside a logarithm; we wrote it as $C D^2(\rho + \log T)$. The theorem on a component has "short basis" in its second name, but its proof builds no basis: the short bases are part of the geometric hypotheses, which are passed on unchanged, and only the fields on birationality and total complexity are used ([HilbertSamuelComponentShortBasisBound.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertSamuelComponentShortBasisBound.lean#L26)). The arguments $J$ and $j_0$ of the claim are always $\log \Lambda_0$ and $1$. The proof ends with one `rw` with the equalities of the presentation. We have not unfolded the presentation, the image degree, the component height or the lattice degree, so we do not show why they agree with the numbers of $X$.
