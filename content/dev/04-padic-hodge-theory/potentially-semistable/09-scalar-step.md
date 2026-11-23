---
title: From an A_inf coboundary to a crystalline cocycle
decls:
  - GlobalTheory.Cyc.ClassBound.scalar_step
  - GlobalTheory.Cyc.ClassBound.scalar_of_isCob
status: drafted
drafted_by: writer@claude-opus-5-5
---
## From an $A_{\inf}$ coboundary to a crystalline cocycle

Let $c$ be a scalar cocycle of $G_{K_s}$ with values in $\mathbb{Q}_\ell(-e)$, known only up to $\mathbb{Z}_\ell$, and assume that some multiple $\ell^N c$ becomes a coboundary modulo $\mathrm{Fil}^{e+1}$ with coefficients in $A_{\inf}$. This section proves that a fixed power of $\ell$ times $c$ is congruent modulo $\mathbb{Z}_\ell$ to a true cocycle that is a coboundary in $B$, that is, to a crystalline cocycle. The exponent depends only on $N$, $\ell$, $s$ and $e$. The proof has three steps: lift $c$ to a true cocycle, subtract a cocycle with the same dual exponential by [Theorem 6.8.6](/entry/exp-star-image/), and use that a cocycle with dual exponential $0$ is crystalline. The result, in the form of [Lemma 6.9.6](/entry/scalar-of-is-cob/) below, is the step from $A_{\inf}$ to $B$ in [Lemma 6.6.5](/entry/mem-hf-d-of-is-cob/), one coordinate at a time. We use [local Bloch-Kato theory](/learn/padic-hodge/#local-bloch-kato-theory) and [[Galois cohomology|9MPCZ3EAJM]] of [local fields](/learn/galois-cohomology/#local-fields).

We keep the notation of the previous section, for the local period data at $\ell$ of a fixed datum, with its $A_{\inf}$ data and its tie. We write $\iota : A_{\inf} \to B_{\mathrm{dR}}$ also for the composite of the map $A_{\inf} \to B$ of the $A_{\inf}$ data with $\iota : B \to B_{\mathrm{dR}}$. Let $K$ be a finite extension of $\mathbb{Q}_\ell$, let $s \geq 1$ with $s \geq 2$ if $\ell = 2$, and let $e \in \mathbb{N}$. Put
$$a(s, e) = (e + 2) s + v_\ell(e) + \lfloor e/(\ell - 1) \rfloor + 1, \qquad \lambda(s, e) = s + v_\ell(e + 1),$$
with the convention $v_\ell(0) = 0$. For $N \in \mathbb{N}$ the number $N + a(s, e) + \lambda(s, e)$ is the number $k = c(N) - g_K$ of [Lemma 6.6.5](/entry/mem-hf-d-of-is-cob/).

**Definition 6.9.1 (Integral modulo $\mathrm{Fil}^{e+1}$).** A map $z : G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$ is *$A_{\inf}$-integral in weight $e$ on $G_{K_s}$* if there is $b \in \mathrm{Fil}^0 B_{\mathrm{dR}}$ such that for every $\sigma \in G_{K_s}$ there is $a_\sigma \in A_{\inf}$ with
$$z(\sigma) - \big( \chi(\sigma)^{-e} \sigma(b) - b \big) - \iota(a_\sigma) \in \mathrm{Fil}^{e+1} B_{\mathrm{dR}}.$$

So $z$ is a coboundary in $\mathrm{Fil}^0 B_{\mathrm{dR}} / \mathrm{Fil}^{e+1}$ for the twisted action, up to elements of the image of $A_{\inf}$. Every map with values in $\mathbb{Z}_\ell$ has this property with $b = 0$, and the property is stable under sums and under multiplication by elements of $\mathbb{Z}_\ell$.

**Lemma 6.9.2 (Lifting an almost cocycle).** Assume local Tate duality. Let $r \in \mathbb{N}$ and $c : G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$, and assume for $\sigma, \tau \in G_{K_s}$:

1. $|c(\sigma)| \leq \ell^r$;
2. $|c(\sigma\tau) - c(\sigma) - \chi(\sigma)^{-e} c(\tau)| \leq 1$;
3. $|c(\tau) - c(\sigma)| \leq 1$ for all $\tau \in G_{K_s}$ near $\sigma$.

Then there is a continuous cocycle $z : G_{K_s} \to \mathbb{Q}_\ell(-e)$ with $|z(\sigma) - \ell^{\lambda(s,e)} c(\sigma)| \leq 1$ for $\sigma \in G_{K_s}$.

Lean: `GlobalTheory.Cyc.TwistLift.lift_cocycle`.

*Proof.* This is a result proved elsewhere in this development from local Tate duality, applied to the cyclotomic character of the period data. $\square$

The map $c$ modulo $\mathbb{Z}_\ell$ is a locally constant cocycle with values in $(\mathbb{Q}_\ell/\mathbb{Z}_\ell)(-e)$. The obstruction to lifting it lies in $H^2(G_{K_s}, \mathbb{Z}_\ell(-e))$. The factor $\ell^{\lambda(s,e)}$ is the order of $H^0(G_{K_s}, (\mathbb{Q}_\ell/\mathbb{Z}_\ell)(e+1))$, since $\chi(G_{K_s}) = 1 + \ell^s \mathbb{Z}_\ell$ and $v_\ell((1 + \ell^s)^{e+1} - 1) = s + v_\ell(e+1)$; by local Tate duality this group controls the torsion of that $H^2$.

**Lemma 6.9.3 (Dual exponential zero).** Assume local Tate duality and the local Euler characteristic formula. If $z$ has dual exponential $0$ in weight $e$ on $G_{K_s}$, then there is $x \in B$ with $z(\sigma) = \chi(\sigma)^{-e} \sigma(x) - x$ in $B$ for all $\sigma \in G_{K_s}$.

Lean: `GlobalTheory.T.coboundary_bcris_of_dualExponential_zero`.

*Proof.* This is a result proved elsewhere in this development. $\square$

**Lemma 6.9.4 (Approximation by a cocycle with dual exponential zero).** Assume local Tate duality and the local Euler characteristic formula. Let $z : G_{K_s} \to \mathbb{Q}_\ell(-e)$ be a continuous cocycle that is $A_{\inf}$-integral in weight $e$ on $G_{K_s}$. Then there is $z'$ with dual exponential $0$ in weight $e$ on $G_{K_s}$ such that
$$|z'(\sigma) - \ell^{a(s,e)} z(\sigma)| \leq 1 \qquad (\sigma \in G_{K_s}).$$

Lean: `GlobalTheory.Cyc.ExpScalar.exists_expStar_zero_near`.

*Proof.* Two results proved elsewhere in this development describe the dual exponential at level $s$. First, every continuous cocycle $z : G_{K_s} \to \mathbb{Q}_\ell(-e)$ has dual exponential $\alpha$ in weight $e$ for exactly one $\alpha \in K_s$. Second, if $z$ is also $A_{\inf}$-integral, then
$$|\alpha| \leq \ell^{\, e(s+1) + v_\ell(e!) + 1 + s + e/(\ell-1)}.$$
Put $a = a(s, e)$ and $\beta = \beta(s, e)$, as in the previous section. A direct estimate of the exponents gives
$$e(s+1) + v_\ell(e!) + 1 + s + \frac{e}{\ell - 1} \leq a - \beta.$$
For $e = 0$ the two sides are $s + 1$ and $2s + 2$. For $e \geq 1$ use $v_\ell(e!) = v_\ell(e) + v_\ell((e-1)!)$ and $e/(\ell-1) \leq \lfloor e/(\ell-1) \rfloor + 1$. So $\ell^{a - \beta} \alpha$ lies in $K_s$ and has norm at most $1$. By [Theorem 6.8.6](/entry/exp-star-image/) there is $z_1$ with $|z_1| \leq 1$ on $G_{K_s}$ and dual exponential $\ell^\beta \ell^{a - \beta} \alpha = \ell^a \alpha$. The dual exponential condition is linear: if $z$ has dual exponential $\alpha$ and $z_1$ has $\alpha_1$, then $c z - z_1$ has $c \alpha - \alpha_1$ for $c \in \mathbb{Q}_\ell$, with the element $c b - b_1$ of $\mathrm{Fil}^0 B_{\mathrm{dR}}$. So $z' = \ell^a z - z_1$ has dual exponential $0$, and $|z' - \ell^a z| = |z_1| \leq 1$ on $G_{K_s}$. $\square$

**Lemma 6.9.5 (The scalar step).** Assume local Tate duality and the local Euler characteristic formula. Let $r, N \in \mathbb{N}$ and $c : G_{\mathbb{Q}_\ell} \to \mathbb{Q}_\ell$. Assume that $c$ satisfies the conditions 1, 2 and 3 of the Lemma on lifting, and that $\ell^N c$ is $A_{\inf}$-integral in weight $e$ on $G_{K_s}$. Then there are a continuous cocycle $z : G_{K_s} \to \mathbb{Q}_\ell(-e)$ and $x \in B$ such that, for all $\sigma \in G_{K_s}$,
$$z(\sigma) = \chi(\sigma)^{-e} \sigma(x) - x \ \text{ in } B, \qquad |z(\sigma) - \ell^{N + a(s,e) + \lambda(s,e)} c(\sigma)| \leq 1.$$

Lean: `GlobalTheory.Cyc.ClassBound.scalar_step`.

*Proof.* Put $\lambda = \lambda(s, e)$ and $a = a(s, e)$. The Lemma on lifting gives a continuous cocycle $z_0$ with $z_0 = u + \ell^\lambda c$ on $G_{K_s}$, where $u(\sigma) \in \mathbb{Z}_\ell$. Then $\ell^N z_0$ is a continuous cocycle. It is $A_{\inf}$-integral in weight $e$. Indeed, let $b$ and $a_\sigma$ be the elements for $\ell^N c$. Since $\mathbb{Z}_\ell \to A_{\inf} \to B_{\mathrm{dR}}$ is the inclusion $\mathbb{Z}_\ell \subseteq B_{\mathrm{dR}}$, the elements $\ell^\lambda b$ and $\ell^\lambda a_\sigma + \ell^N u(\sigma)$ work for $\ell^N z_0 = \ell^\lambda (\ell^N c) + \ell^N u$, because $\mathrm{Fil}^0$ and $\mathrm{Fil}^{e+1}$ are stable under multiplication by integers. The Lemma on approximation gives $z$ with dual exponential $0$ and $|z - \ell^{a} \ell^N z_0| \leq 1$ on $G_{K_s}$. The Lemma on dual exponential zero gives $x \in B$ with $z(\sigma) = \chi(\sigma)^{-e} \sigma(x) - x$. Finally
$$z - \ell^{N + a + \lambda} c = \big(z - \ell^{a} \ell^N z_0\big) + \ell^{a + N} \big(z_0 - \ell^\lambda c\big),$$
and both terms have norm at most $1$ on $G_{K_s}$, so the ultrametric inequality gives the bound. $\square$

The next form of the scalar step starts from a cocycle with values in a $\mathbb{Z}_\ell$-module $Y$ and a linear form on $Y$. It is the form used for the coordinates of a lattice. Recall $A_{\inf}[0, e+1) = A_{\inf} / \xi^{e+1} A_{\inf}$, and let $Y \otimes_{\mathbb{Z}_\ell} A_{\inf}[0, e+1)$ carry the diagonal action of $G_{K_s}$.

**Lemma 6.9.6 (The scalar step for an $A_{\inf}$ coboundary).** Assume local Tate duality and the local Euler characteristic formula. Assume $G_{K_s} \subseteq G_K$. Let $N, r \in \mathbb{N}$. Let $Y$ be a $\mathbb{Z}_\ell$-module with a $\mathbb{Z}_\ell$-linear action $\rho$ of $G_K$, and let $f : G_K \to Y$ satisfy $f(gh) = f(g) + \rho(g) f(h)$. Assume:

1. for each $n \in \mathbb{N}$ and $g \in G_K$, $f(h) - f(g) \in \ell^n Y$ for all $h$ near $g$;
2. the map $g \mapsto \ell^N \big( f(g) \otimes 1 \big)$ on $G_{K_s}$ is a coboundary in $Y \otimes_{\mathbb{Z}_\ell} A_{\inf}[0, e+1)$;
3. $\psi : Y \to \mathbb{Q}_\ell$ is $\mathbb{Z}_\ell$-linear, $|\psi(y)| \leq \ell^r$, and $|\psi(\rho(g) y) - \chi(g)^{-e} \psi(y)| \leq 1$ for $g \in G_K$ and $y \in Y$.

Then there are a continuous cocycle $z : G_{K_s} \to \mathbb{Q}_\ell(-e)$ and $x \in B$ such that, for all $g \in G_{K_s}$,
$$z(g) = \chi(g)^{-e} g(x) - x \ \text{ in } B, \qquad |z(g) - \ell^{N + a(s,e) + \lambda(s,e)} \psi(f(g))| \leq 1.$$

Lean: `GlobalTheory.Cyc.ClassBound.scalar_of_isCob`.

*Proof.* Let $c = \psi \circ f$ on $G_K$ and $c = 0$ outside $G_K$. We check the hypotheses of the scalar step. Condition 1 holds since $|\psi| \leq \ell^r$. For condition 2, the cocycle identity of $f$ gives $c(\sigma\tau) - c(\sigma) - \chi(\sigma)^{-e} c(\tau) = \psi(\rho(\sigma) f(\tau)) - \chi(\sigma)^{-e} \psi(f(\tau))$, which has norm at most $1$. For condition 3, take $n = r$ in hypothesis 1: for $\tau$ near $\sigma$ we have $f(\tau) - f(\sigma) = \ell^r y$, so $|c(\tau) - c(\sigma)| = \ell^{-r} |\psi(y)| \leq 1$. It remains to see that $\ell^N c$ is $A_{\inf}$-integral in weight $e$. A result proved elsewhere in this development pushes the coboundary of hypothesis 2 forward along $\psi$. Write $\ell^N (f \otimes 1) = \delta X$ with $X \in Y \otimes A_{\inf}[0, e+1)$. The map $\ell^r \psi$ is integral, so it sends $X$ to a class in $A_{\inf}[0, e+1)$; let $a_0 \in A_{\inf}$ lift it. Then $b = \ell^{-r} \iota(a_0) \in \mathrm{Fil}^0 B_{\mathrm{dR}}$ is the element of the definition, for every $\sigma \in G_{K_s}$. The scalar step now gives $z$ and $x$, and on $G_{K_s}$ we have $c = \psi \circ f$. $\square$

**Remark 6.9.7 (Formalization).** All four Lemmas take local Tate duality `adm2 D` and the local Euler characteristic formula `ArchimedeanSignatureMatching D` as hypotheses. The Lemma on lifting uses only local Tate duality: its proof `fun D h2 _ l _ K s hs e _ c _ hc hloc` at [ContinuousFixingSubgroupEquiv.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ContinuousFixingSubgroupEquiv.lean#L385) also drops $r$ and the bound $|c| \leq \ell^r$. The Lemma on approximation discards both inputs in its intro at [ExistsExpStarZeroNear.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsExpStarZeroNear.lean#L60). The Lemma on dual exponential zero is a `first | exact ...` wrapper of `GlobalTheory.KerExpCrys.cob_cris_of_expStar_zero`, whose proof we did not open. We did not open the proofs of `lift_cocycle_of_duality`, `GlobalTheory.T.dualExponential_existsUnique_cyclotomicLevel` or `GlobalTheory.T.norm_dualExponential_le_of_ainf_valued`, and we read only the first lines of `GlobalTheory.PushCob.push_coboundary`. The sentence after the Lemma on lifting explains the factor $\ell^{\lambda(s,e)}$; it is not a statement of the development. In the last Lemma the map $c$ is extended by $0$ outside $G_K$ ([CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L221)); only its values on $G_{K_s}$ matter. The coefficient $1$ of hypothesis 2 is an element `one` of $\xi^0 A_{\inf}$ with image $1$ in $W(\mathbb{C}^\flat)$, given as an argument.
