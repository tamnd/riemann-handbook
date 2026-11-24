---
title: Cutting vertical divisors and blow-ups
decls:
  - GlobalTheory.T.cut_effective_divisor
  - GlobalTheory.CompanionTheory.Ar.Num.CutClosed.main
  - GlobalTheory.CompanionTheory.Ar.Num.CutClosed.verticalPush
  - GlobalTheory.T.blow_up_fibre_semilocal
  - GlobalTheory.CompanionTheory.CommAlg.BlowUpFibre.main
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Cutting vertical divisors and blow-ups

The Chern numbers of flag models are intersection numbers of divisors on models over a discrete valuation ring. This section proves the basic identity that lets us compute them one divisor at a time: the intersection of a vertical divisor with an effective divisor $\operatorname{div}(s)$ can be computed on the components of $\operatorname{div}(s)$. It is the arithmetic form of the commutativity of intersection with Cartier divisors. The identity gives the commutativity of two vertical divisors, which enters [the independence of the flag pair](/entry/flag-independence-main/), and it is used in [the cut of a Segre flag](/entry/segre-flag-closure-cut/) of the next section. Its proof needs a blow-up, and we prove here the local fact on blow-ups that it uses: the points of a blow-up over a vertical point are the maximal ideals of a finite birational extension of a one dimensional local ring.

### Models and cycles

Let $O$ be a discrete valuation ring with uniformizer $\varpi$ and residue field $k$. Let $K$ be a finite set, and for each $j \in K$ let $\iota_j$ be a finite set of variables. Let $A = O[x_{j,i} : j \in K, i \in \iota_j]$, graded by multidegree in $\mathbb{N}^K$: the variable $x_{j,i}$ has degree $e_j$. An ideal of $A$ is relevant if for each $j$ it does not contain all the variables $x_{j,i}$. So a relevant multihomogeneous prime of $A$ is a point of the product of projective spaces $\prod_j \mathbb{P}^{\iota_j}_O$.

**Definition 5.7.1 (Model).** A model of relative dimension $d$ is a relevant multihomogeneous prime $P$ of $A$ with $P \cap O = 0$ and $\dim A/P = d + 1 + |K|$.

Lean: `GroundTheory.Heights₂.Heights.NumbersDVR.IsModelOver`.

So $P$ is an integral closed subscheme of $\prod_j \mathbb{P}^{\iota_j}_O$, flat over $O$, of dimension $d + 1$.

**Definition 5.7.2 (Divisors and intersection numbers).** Let $P$ be a prime and $h \in A$. The divisor $\operatorname{div}_P(h)$ gives each relevant minimal prime $W$ of $P + (h)$ the length of $(A/(P + (h)))_W$ over $A_W$, and every other prime the value $0$. For $f, g \in A$ put $\operatorname{div}_P(f/g) = \operatorname{div}_P(f) - \operatorname{div}_P(g)$, and write $\operatorname{ord}_W$ for the value at $W$. For a prime $W$ and degrees $a_1, \dots, a_n \in \mathbb{Z}^K$, let $\chi_W$ be the Hilbert function of the special fibre $W \otimes k$, and put
$$v(W; a_1, \dots, a_n) = \lim_{m \to \infty} (\Delta_{a_1} \cdots \Delta_{a_n} \chi_W)(m), \qquad (\Delta_a h)(m) = h(m) - h(m - a),$$
where the limit is the eventual value along $m \to \infty$ in $\mathbb{Z}^K$, and is $0$ when the function is not eventually constant.

Lean: `GroundTheory.Heights₂.Heights.NumbersDVR.divCycle` (also `ratDiv`, `cycEval`, `vNum` and `intNum`).

When $W$ has relative dimension $n - 1$, the number $v(W; a_1, \dots, a_n)$ is the intersection number on the special fibre of $W$ of the line bundles $\mathcal{O}(a_1), \dots, \mathcal{O}(a_n)$ (Kleiman, see the Notes). The theorem below only uses the definition.

**Definition 5.7.3 (Vertical divisor).** Let $P$ be a prime and $b \in \mathbb{Z}^K$. A pair $f, g \in A$ is a vertical divisor of degree $b$ on $P$ if $f$ and $g$ are multihomogeneous, not in $P$, with $\deg f - \deg g = b$; every prime $W$ with $\operatorname{ord}_W(f/g) \neq 0$ contains $\varpi$; and for every relevant prime $W \supseteq P$ with $\varpi \notin W$ there are $u, v \notin W$ with $uf - vg \in P$.

Lean: `GroundTheory.Heights₂.Heights.NumbersDVR.IsVerticalDivisor`.

The last condition says that $f/g$ is a unit on the generic fibre near $W$. For example $\varpi/1$ is a vertical divisor of degree $0$, and $\operatorname{div}_P(\varpi)$ is the special fibre of $P$.

**Theorem 5.7.4 (Cutting a vertical divisor).** Let $P$ be a model of relative dimension $d + 1$, let $f/g$ be a vertical divisor of degree $b$ on $P$, and let $s \notin P$ be multihomogeneous of degree $c$. Assume that $f/g$ is a vertical divisor of degree $b$ on each prime $H$ with $\operatorname{ord}_H(s) \neq 0$ and $\varpi \notin H$. Then for all $L = (a_1, \dots, a_d)$ in $\mathbb{Z}^K$,
$$\begin{aligned}
\sum_G \operatorname{ord}_G(f/g)\, v(G; c, L) &= \sum_{W \ni \varpi} \operatorname{ord}_W(s)\, v(W; b, L) \\
&\quad + \sum_{W \not\ni \varpi} \operatorname{ord}_W(s) \sum_G \operatorname{ord}^W_G(f/g)\, v(G; L).
\end{aligned}$$
Here $\operatorname{ord}_W(s)$ is taken on $P$, and $\operatorname{ord}^W_G(f/g)$ is the value at $G$ of $\operatorname{div}_W(f/g)$.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CutClosed.main` (also `GlobalTheory.T.cut_effective_divisor`, a second name).

The left side is the intersection of $\operatorname{div}(f/g)$ with $\operatorname{div}(s)$ and $L$. On the right, the vertical components $W$ of $\operatorname{div}(s)$ meet $f/g$ through its degree $b$ only, and the horizontal components meet it through the restriction of $f/g$.

*Proof.* There are four steps. First, there is $n \ge 0$ such that $\varpi^n f / g$ is effective: at every relevant prime $W \supseteq P$ there are $u \notin W$ and $v$ with $u \varpi^n f - v g \in P$. Second, the identity holds for the divisor $\varpi/1$. Third, both sides are additive in the vertical divisor, so the identity for $f/g$ follows from those for $\varpi^n f/g$ and $\varpi/1$. It remains to prove the identity for an effective vertical divisor $f/g$.

For this we use strong induction on the common excess, the largest value of $\operatorname{ord}_G(s) \operatorname{ord}_G(f/g)$ over the primes $G \ni \varpi$. If it is $0$, no vertical component of $\operatorname{div}(s)$ is a component of $\operatorname{div}(f/g)$, and a separate lemma proves the identity in this case. If it is positive, we blow up the model along an ideal generated by forms $u_j$ of one degree $N$. The blow-up is again a model of the same relative dimension. The strict transforms of $s$ and $f/g$ have smaller common excess, so the identity holds on the blow-up by induction. We then move each side back to $P$. The vertical part of a divisor moves back by the lemma on vertical push forward below, and the horizontal parts by a correspondence between the horizontal components on the two models. The induction runs over all models, with any set of blocks and any dimension. $\square$

### Blow-ups

**Definition 5.7.5 (Blow-up).** Let $P$ be a prime of $A$ and let $u = (u_j)_{j \in J}$ be forms of degree $N$, not all in $P$. Let $A' = A[y_j : j \in J]$, with the variables $y_j$ in one new block, so that $A'$ is graded by $\mathbb{N}^{\{\ast\} \sqcup K}$. The blow-up of $P$ along $u$ is the kernel $\tilde P$ of the map $A' \to (A/P)[t]$ with $x_{j,i} \mapsto x_{j,i}$ and $y_j \mapsto u_j t$. A form $h$ of $A$ is also a form of $A'$, and a degree $a \in \mathbb{Z}^K$ is also a degree in $\mathbb{Z}^{\{\ast\} \sqcup K}$, with $0$ on the new block.

Lean: `GroundTheory.Heights₂.Heights.NumbersDVR.blowUpOf` (also `liftForm` and `liftDegs`).

Here $\tilde P$ is the graph of the rational map $[u_j]$ from $P$ to $\mathbb{P}^J$, so it is the blow-up of $P$ along the ideal of the $u_j$.

**Definition 5.7.6 (Homogeneous local ring).** Let $P \subseteq W$ be primes of $A$. The homogeneous local ring $\mathcal{O}_{P, W}$ is the subring of the fraction field of $A/P$ generated by the fractions $f/g$ with $f, g$ multihomogeneous of the same degree and $g \notin W$.

Lean: `GroundTheory.Heights₂.Heights.NumbersDVR.homLocRing`.

It is the local ring of the scheme $P$ at the point $W$. For a prime $W'$ of $A'$ we write $\delta(W')$ for the degree of the field of degree $0$ fractions of the special fibre of $W'$ over that of its contraction to $A$, and $0$ when the special fibre of $W'$ is not prime.

**Theorem 5.7.7 (Semilocal ring of a blow-up).** Let $P$ be a model of relative dimension $n$, let $u$ be forms of degree $N$ not all in $P$, and let $x \notin P$ be multihomogeneous of degree $c$. Let $W$ be a relevant minimal prime of $P + (x)$ with $\varpi \in W$, and let $g \notin W$ be multihomogeneous of degree $c$, so that $z = x/g$ lies in $\mathcal{O}_{P,W}$. Then there is a domain $B$ that is a finite extension of $\mathcal{O}_{P,W}$ of rank $1$, with $\mathcal{O}_{P,W} \to B$ injective, and a bijection $\mathfrak{n} \mapsto W'_{\mathfrak{n}}$ from the maximal ideals of $B$ to the relevant minimal primes $W'$ of $\tilde P + (x)$ with $W' \cap A = W$, such that for each $\mathfrak{n}$
$$\operatorname{length}\, B_{\mathfrak n}/(z) = \operatorname{ord}_{W'_{\mathfrak n}}(x), \qquad f(\mathfrak{n} \mid \mathfrak{m}) = \delta(W'_{\mathfrak n}).$$
Here $\operatorname{ord}$ is taken on $\tilde P$, and $f(\mathfrak{n} \mid \mathfrak{m})$ is the residue degree of $\mathfrak{n}$ over the maximal ideal $\mathfrak{m}$ of $\mathcal{O}_{P,W}$.

Lean: `GlobalTheory.CompanionTheory.CommAlg.BlowUpFibre.main` (also `GlobalTheory.T.blow_up_fibre_semilocal`, a second name).

*Proof.* Take for $B$ the intersection, in the fraction field of $A/P$, of the homogeneous local rings of $\tilde P$ at all relevant multihomogeneous primes $Q \supseteq \tilde P$ with $Q \cap A \subseteq W$. This is the semilocal ring of the blow-up along the fibre over $W$. The ring $\mathcal{O}_{P,W}$ is local and noetherian of dimension $1$, since $W$ is a minimal prime over $P + (x)$. The ring $B$ is finite over it, by the finiteness of a blow-up over a point; it has rank $1$, since both rings have the fraction field of $A/P$. The maximal ideals of $B$ correspond to the closed points of the fibre over $W$, which are the relevant minimal primes $W'$ of $\tilde P + (x)$ over $W$. At each of them the localization of $B$ is the homogeneous local ring $\mathcal{O}_{\tilde P, W'}$. So the length of $B_{\mathfrak n}/(z)$ is the length of $\mathcal{O}_{\tilde P, W'}/(x/g)$, which is $\operatorname{ord}_{W'}(x)$ by the comparison of lengths on the cone and in the homogeneous local ring. Last, the residue field of $B_{\mathfrak n}$ is the field of degree $0$ fractions of the special fibre of $W'$, and that of $\mathcal{O}_{P,W}$ is the same field for $W$. This gives $f(\mathfrak n \mid \mathfrak m) = \delta(W')$. $\square$

**Lemma 5.7.8 (Vertical push forward).** Let $P$ be a model of relative dimension $n$, let $u$ be forms of degree $N$ not all in $P$, and let $x \notin P$ be multihomogeneous. Then for all $a = (a_1, \dots, a_n)$ in $\mathbb{Z}^K$,
$$\sum_{W' \ni \varpi} \operatorname{ord}_{W'}(x)\, v(W'; a) = \sum_{W \ni \varpi} \operatorname{ord}_W(x)\, v(W; a),$$
where on the left $\operatorname{ord}$ is taken on the blow-up $\tilde P$ and $a$ has degree $0$ on the new block.

Lean: `GlobalTheory.CompanionTheory.Ar.Num.CutClosed.verticalPush`.

*Proof.* The blow-up $\tilde P$ is a model of relative dimension $n$. Fix a vertical prime $W$ with $\operatorname{ord}_W(x) \neq 0$. Apply the theorem on the semilocal ring with $z = x/g$. The length formula for a finite birational extension of a one dimensional noetherian local domain gives
$$\operatorname{length}\, \mathcal{O}_{P,W}/(z) = \sum_{\mathfrak n} \operatorname{length}\, B_{\mathfrak n}/(z) \cdot f(\mathfrak n \mid \mathfrak m).$$
The left side is $\operatorname{ord}_W(x)$, by the comparison of lengths. So $\sum_{W' \mapsto W} \operatorname{ord}_{W'}(x)\, \delta(W') = \operatorname{ord}_W(x)$. The projection formula for degrees says that $v(W'; a) = \delta(W')\, v(W; a)$ when $W'$ lies over $W$ and both have the same dimension. Multiply by $v(W; a)$ and sum over $W$. $\square$

**Remark 5.7.9.** The length formula is the formula $e(z, \mathcal{O}) = \sum_{\mathfrak n} e(z, B_{\mathfrak n})\, [\kappa(\mathfrak n) : \kappa(\mathfrak m)]$ for a finite extension of rank $1$ (Fulton, *Intersection Theory*, Appendix A).

**Remark 5.7.10 (Formalization).** The lemma on vertical push forward is a local lemma of the proof of the theorem on cuts ([CutEffectiveDivisor.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/CutEffectiveDivisor.lean#L19)). The theorem on the semilocal ring is a direct alias of a theorem in the folder of the Weil bound ([XSBlowupfibre.lean](lean:Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/XSBlowupfibre.lean#L355)). It requires $B$ to have rank $1$, which is the birational case only. The second names call the first with `first | exact @…` and fix the universe to $0$. We did not open the proofs of the steps of the induction, the lemma for divisors with no common component, or the lemmas on finiteness, localization and lengths that the proofs cite; we give their statements as they enter.
