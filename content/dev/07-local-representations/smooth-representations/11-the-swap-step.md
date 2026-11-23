---
title: The swap step for unitary groups
decls:
  - GlobalTheory.CompanionTheory.SwapRoot.swapStepU
  - GlobalTheory.CompanionTheory.SwapRoot.step_borel_shift
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The swap step for unitary groups

The previous section stated the swap reduction: an injective $G$-map from an irreducible spherical representation into $I(\alpha)$ gives one into $I(\alpha')$, where $\alpha'$ exchanges two neighbouring parameters $\alpha_i$ and $\alpha_{i+1}$ with $|\alpha_i/\alpha_{i+1}| < 1$. This section proves it. The new map is an intertwining integral over a one-parameter root group. The integral is a functional on a class of functions on $L$ with a fixed behaviour at infinity, and its value on the spherical vector is a rank one factor $(1 - w)/(1 - wq^2)$. The result feeds the embedding theorem [Theorem 7.7 of Volume 8](/entry/extreme-u/), which puts the parameters of an unramified representation in a fixed order. For background see [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Setting

We keep the unramified setting of the previous section: the extension $L$ with the involution $\sigma$, the uniformizer $\varpi$, the residue field with $q^2$ elements, the unitary group $G$ of the antidiagonal form, its integral subgroup $K$, the upper triangular group $B$, the upper unipotent group $N$, $m = \lfloor n/2 \rfloor$, the character $\chi_\alpha$ of $B$ and the space $I(\alpha)$. We write $\mathrm{ord}$ for the normalized valuation of $L$, so $\mathrm{ord}(\varpi) = 1$, and $\mathcal{O}$ for the ring of integers.

Fix $1 \leq i < m$. For $\alpha \in (\mathbb{C}^\times)^m$ let $\alpha'$ be $\alpha$ with $\alpha_i$ and $\alpha_{i+1}$ exchanged, and put
$$w = \frac{\alpha_i/\alpha_{i+1}}{q^2}.$$
Then $w \neq 0$, and the condition $|\alpha_i/\alpha_{i+1}| < 1$ is the condition $|w|\,q^2 < 1$.

### Functions on the line

The intertwining integral is an integral over a copy of $L$. The integrand is a locally constant function that agrees with a power of $w$ far out. The next definition names this class.

**Definition 1.11.1 (Admissible function).** Let $w \in \mathbb{C}$. A function $F \colon L \to \mathbb{C}$ is *$w$-admissible* if it is locally constant and there are $R \in \mathbb{Z}$ and $C \in \mathbb{C}$ with $F(x) = C\,w^{-\mathrm{ord}(x)}$ for all $x \neq 0$ with $\mathrm{ord}(x) \leq R$.

**Definition 1.11.2 (Spherical function on the line).** For $w \in \mathbb{C}^\times$ let $\phi_w \colon L \to \mathbb{C}$ be $\phi_w(x) = 1$ for $x \in \mathcal{O}$ and $\phi_w(x) = w^{-\mathrm{ord}(x)}$ otherwise.

The function $\phi_w$ is $w$-admissible, with $R = -1$ and $C = 1$. A $w$-admissible function is bounded on each compact set, and for $|x|$ large it has size $|w|^{k}$ on the shell $\mathrm{ord}(x) = -k$. That shell has Haar measure $q^{2k} - q^{2k-2}$ when $\mathcal{O}$ has measure $1$. So the Haar integral converges when $|w|\,q^2 < 1$, and on $\phi_w$ it gives
$$1 + \sum_{k \geq 1}\big(q^{2k} - q^{2k-2}\big)w^k = 1 + \big(1 - q^{-2}\big)\frac{wq^2}{1 - wq^2} = \frac{1 - w}{1 - wq^2}.$$
We take this functional as given, in the following form.

### The inputs

We take the following facts as given; they are proved elsewhere in the development. Let $a = i$ be the position of the swap. There is a continuous map $u \colon L \to G$ with $u(0) = 1$ and $u(x + y) = u(x)u(y)$, the root group of the simple root between positions $i$ and $i+1$, and an element $s \in G$ with $s^2 = 1$, a reflection for that root.

**Theorem 1.11.3 (Inputs for the swap step).** Assume the unramified setting, and let $|w|\,q^2 < 1$, $w \neq 0$.

- (i) There is a map $\Lambda$ from functions $L \to \mathbb{C}$ to $\mathbb{C}$ such that, for $w$-admissible $F$ and $F'$: $\Lambda(F + F') = \Lambda(F) + \Lambda(F')$ and $\Lambda(cF) = c\Lambda(F)$ for $c \in \mathbb{C}$; for $y \in L$, $x \mapsto F(x + y)$ is $w$-admissible with the same value of $\Lambda$; for $c \in L^\times$, $x \mapsto F(cx)$ is $w$-admissible and $\Lambda(x \mapsto F(cx)) = q^{2\,\mathrm{ord}(c)}\Lambda(F)$. Also $\phi_w$ is $w$-admissible and $\Lambda(\phi_w) = (1 - w)/(1 - wq^2)$.
- (ii) $s \in K$, and $u(x) \in K$ for $x \in \mathcal{O}$.
- (iii) For $x \neq 0$ there is $b \in B$ with $\chi_\alpha(b) = w^{-\mathrm{ord}(x)}$ and $s\,u(x) = b\,s\,u(x^{-1})\,s$.
- (iv) For $v \in N$ there is $y \in L$ such that for every $x$ there is $b \in N$ with $s\,u(x)\,v = b\,s\,u(x + y)$.
- (v) For diagonal $t \in G$ there are $c \in L^\times$ and $t' \in B$ with $s\,u(x)\,t = t'\,s\,u(cx)$ for all $x$, and $\chi_\alpha(t')\,q^{2\,\mathrm{ord}(c)} = \chi_{\alpha'}(t)$.
- (vi) Every $b \in B$ is $tv$ with $t$ diagonal in $G$ and $v \in N$. The character $\chi_\alpha$ is multiplicative on $B$ and trivial on $N$. Also $G = BK$.

Fact (iii) is a rank one computation in the Levi subgroup of the root. It is the reason why $w$, and not $\alpha_i/\alpha_{i+1}$, appears: the factor $q^{-2}$ is the modulus character on the root.

**Lemma 1.11.4 (Borel shift).** Let $b \in B$. There are $c \in L^\times$, $y \in L$ and $C \in \mathbb{C}$ such that for every $x \in L$ there is $b' \in B$ with $\chi_\alpha(b') = C$ and
$$s\,u(x)\,b = b'\,s\,u(cx + y),$$
and $C\,q^{2\,\mathrm{ord}(c)} = \chi_{\alpha'}(b)$.

Lean: `GlobalTheory.CompanionTheory.SwapRoot.step_borel_shift`.

*Proof.* Write $b = tv$ by (vi). Fact (iv) for $v$ gives $y$. Fact (v) for $t$ gives $c$ and $t'$. Put $C = \chi_\alpha(t')$. For $x \in L$, (iv) at the point $cx$ gives $b_0 \in N$ with $s\,u(cx)\,v = b_0\,s\,u(cx + y)$. Then
$$s\,u(x)\,tv = t'\,s\,u(cx)\,v = t'b_0\,s\,u(cx + y).$$
Put $b' = t'b_0$. By (vi), $\chi_\alpha(b') = \chi_\alpha(t') = C$, and $\chi_{\alpha'}(b) = \chi_{\alpha'}(t) = C\,q^{2\,\mathrm{ord}(c)}$ by (v). $\square$

The point of the lemma is that $C$ does not depend on $x$, although $b'$ does.

**Lemma 1.11.5 (Admissibility on the root line).** Let $\varphi \in I(\alpha)$, and let $S \ni 1$ be an open set with $\varphi(gk) = \varphi(g)$ for $k \in S$ and all $g$. Then for every $g \in G$ the function $x \mapsto \varphi(s\,u(x)\,g)$ is $w$-admissible.

*Proof.* Fix $g$. For $y$ near $x$, the element $g^{-1}u(y - x)g$ lies in $S$, by continuity of $u$ and since $u(0) = 1$. As $s\,u(y)\,g = s\,u(x)\,g \cdot g^{-1}u(y - x)g$, the function is constant near $x$. For the tail, $g^{-1}s\,u(z)\,s\,g \to 1$ as $z \to 0$, since $s^2 = 1$. So there is $R$ such that $g^{-1}s\,u(x^{-1})\,s\,g \in S$ whenever $x \neq 0$ and $\mathrm{ord}(x) \leq R$. For such $x$ take $b$ from (iii). Then
$$s\,u(x)\,g = b\,g \cdot g^{-1}s\,u(x^{-1})\,s\,g,$$
so $\varphi(s\,u(x)\,g) = \chi_\alpha(b)\varphi(g) = \varphi(g)\,w^{-\mathrm{ord}(x)}$. This is the required form with $C = \varphi(g)$. $\square$

### The swap step

**Theorem 1.11.6 (Swap step).** Assume the unramified setting. Let $\rho$ be an irreducible admissible representation of $G$ on $V$ with $V^K \neq 0$. Let $\alpha \in (\mathbb{C}^\times)^m$ and $1 \leq i < m$ with $|\alpha_i/\alpha_{i+1}| < 1$, and let $f \colon V \to I(\alpha)$ be an injective $G$-map. Then there is an injective $G$-map $V \to I(\alpha')$.

Lean: `GlobalTheory.CompanionTheory.SwapRoot.swapStepU`.

*Proof.* Write $f_v = f(v)$. Since $f$ is a $G$-map, $f_{\rho(k)v}(g) = f_v(gk)$. Let $\Lambda$ be the functional of (i).

*Step 1: the map.* Fix $v \in V$. As $\rho$ is smooth, $S = \{k : \rho(k)v = v\}$ is open and contains $1$, and $f_v(gk) = f_v(g)$ for $k \in S$. By the lemma on admissibility, $x \mapsto f_v(s\,u(x)\,g)$ is $w$-admissible for every $g$. Put
$$T(v)(g) = \Lambda\big(x \mapsto f_v(s\,u(x)\,g)\big).$$
By (i), $T$ is linear in $v$. Also $T(\rho(k)v)(g) = T(v)(gk)$, since $f_{\rho(k)v}(s\,u(x)\,g) = f_v(s\,u(x)\,gk)$.

*Step 2: the transformation law.* Let $b \in B$ and take $c$, $y$, $C$ from the lemma on the Borel shift. For each $x$, with $b'$ as there,
$$f_v(s\,u(x)\,bg) = f_v(b'\,s\,u(cx + y)\,g) = C\,f_v(s\,u(cx + y)\,g).$$
So the function $x \mapsto f_v(s\,u(x)\,bg)$ is $C$ times the function $F(x) = f_v(s\,u(x)\,g)$ after the translation by $y$ and the scaling by $c$. By (i), translation does not change $\Lambda$, and scaling multiplies it by $q^{2\,\mathrm{ord}(c)}$. Hence
$$T(v)(bg) = C\,q^{2\,\mathrm{ord}(c)}\,T(v)(g) = \chi_{\alpha'}(b)\,T(v)(g).$$
So $T(v) \in I(\alpha')$, and $T \colon V \to I(\alpha')$ is a $G$-map.

*Step 3: the spherical vector.* Let $v_0 \neq 0$ in $V^K$. Then $f_{v_0}(gk) = f_{v_0}(g)$ for $k \in K$. If $f_{v_0}(1) = 0$, then for $g = bk$ with $b \in B$ and $k \in K$ (by (vi)) we get $f_{v_0}(g) = \chi_\alpha(b)f_{v_0}(1) = 0$, so $f_{v_0} = 0$, against the injectivity of $f$. So $f_{v_0}(1) \neq 0$. We claim
$$f_{v_0}(s\,u(x)) = f_{v_0}(1)\,\phi_w(x).$$
If $x \in \mathcal{O}$, then $s\,u(x) \in K$ by (ii), and both sides equal $f_{v_0}(1)$. If $x \notin \mathcal{O}$, then $x^{-1} \in \mathcal{O}$, so $s\,u(x^{-1})\,s \in K$. With $b$ from (iii), $f_{v_0}(s\,u(x)) = \chi_\alpha(b)f_{v_0}(1) = w^{-\mathrm{ord}(x)}f_{v_0}(1)$. This proves the claim. By (i),
$$T(v_0)(1) = f_{v_0}(1)\,\frac{1 - w}{1 - wq^2}.$$
Since $|w| < q^{-2} < 1$, neither $1 - w$ nor $1 - wq^2$ is $0$. So $T(v_0) \neq 0$.

*Step 4: injectivity.* The kernel of $T$ is a subrepresentation of $V$ that does not contain $v_0$. As $\rho$ is irreducible, the kernel is $0$. $\square$

The proof has the same shape as the proof of the inverse reduction in the previous section. The difference is the domain of the integral: here it is one root group, and the integral is the abstract functional $\Lambda$ instead of a measure on a unipotent cell.

**Remark 1.11.7 (Formalization).** The theorem is `SwapStepU` in [SatPowNonvan.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/IwahoriFactorisation/StrictDominance/UnitaryExtremality/SatPowNonvan.lean#L81), proved as `swapStepU` in [UnitarySwapReduction.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/UnitarySwapReduction.lean#L136). The indices are from $0$ in Lean, with $i + 1 = j$, and the position is `a = i.val`. The inputs (i) to (v) are `step_exists_int`, `step_sR_mem_KU`, `step_uR_mem_KU`, `step_factor`, `step_unip_shift` and `step_torus_shift`, each a direct application of a result in `GlobalTheory.T`. The admissibility lemma is `step_stab_adm` (L89). Admissible functions are `IsAdm` and $\phi_w$ is `sphFn`, both in [ConjTransposeAntidiagFixed.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ConjTransposeAntidiagFixed.lean#L347). We have not unfolded the root map `uR` or the reflection `sR`; we use only the listed properties. The functional $\Lambda$ is given abstractly, and its relation to the Haar integral is not part of the statement. Of the admissibility of $\rho$ only smoothness (`hadm.1`) is used.
