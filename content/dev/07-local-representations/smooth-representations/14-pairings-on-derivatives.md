---
title: Pairings on derivatives
decls:
  - GlobalTheory.T.invariant_pairing_mirabolic_smooth
  - GlobalTheory.CompanionTheory.MirPair.pairing_phi
  - GlobalTheory.CompanionTheory.BZCuspPair.pair_iter
  - GlobalTheory.CompanionTheory.BZCuspPair.pair_deriv
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Pairings on derivatives

Let $\pi$ and $\pi'$ be smooth representations of $\mathrm{GL}_N$ over a $p$-adic field with an invariant pairing between them. This section proves that the pairing passes to a pairing between their highest derivatives, with a twist by a power of $|\det|$, and that nondegeneracy is kept. Applied to an invariant Hermitian form, the result says that the highest derivative of a unitary representation carries a nondegenerate invariant form after a twist. This is the step in Bernstein's proof of the classification of the unitary dual of $\mathrm{GL}_n$ that the step [EveryCharacter](/step/every-character/) uses. The main lemma passes a pairing through one application of the functor $\Phi^-$, with an integral over the unipotent radical that becomes constant on large balls.

### Setting

We keep the notation of Sections 5 and 9: $k$ is a nonarchimedean local field, $G_n = \mathrm{GL}_n(k)$, $P_n \subseteq G_n$ is the mirabolic group with unipotent part $U_n \cong k^{n-1}$, and $\theta_\psi(1 + v e_n^{\mathsf{T}}) = \psi(v_{n-1})$. For a character $\psi$ of $k$ we write $\Phi^-_\psi$ for the unnormalized functor $\Phi^-$ built with $\theta_\psi$, and $\Psi^-$ for the unnormalized functor with the trivial character. For $\tau$ a representation of $P_{N}$ put $(\Phi^-_\psi)^0\tau = \tau$ and $(\Phi^-_\psi)^{j+1}\tau = \Phi^-_\psi (\Phi^-_\psi)^j \tau$. For $\pi$ on $G_N$ the unnormalized derivative of Section 9 is $\pi^{(j+1)}_\psi = \Psi^-(\Phi^-_\psi)^j(\pi|_{P_N})$, a representation of $G_{N-j-1}$. Throughout, $\psi$ is a continuous nontrivial character of $k$.

**Definition 1.14.1 (Twisted pairing).** Let $\tau$ and $\tau'$ be representations of a subgroup $H \subseteq G_n$ on $V$ and $V'$, and let $s \in \mathbb{N}$. A bilinear form $B \colon V \times V' \to \mathbb{C}$ is an *$s$-twisted pairing* if
$$B(\tau(h)v, \tau'(h)v') = |\det h|^s\,B(v, v') \qquad (h \in H,\ v \in V,\ v' \in V').$$
It is *left nondegenerate* if for every $v \neq 0$ there is $v'$ with $B(v, v') \neq 0$.

Left nondegeneracy is the only form of nondegeneracy that we need. A $0$-twisted pairing is an invariant pairing.

### One application of Φ

Let $\tau$ and $\tau'$ be smooth representations of $P_{n+2}$ on $V$ and $V'$, and let $B$ be an $s$-twisted pairing. For $x \in k^{n+1}$ let $u_x = 1 + x e_{n+2}^{\mathsf{T}} \in U_{n+2}$. For $t \in k^\times$ let $D_t = \{x \in k^{n+1} : |x_i| \leq |t| \text{ for all } i\}$, and put
$$J_t(v, v') = \int_{D_t} \psi(-x_{n+1})\,B(\tau(u_x)v, v')\,dx$$
with an additive Haar measure. We say that $B$ has *eventual value* $A$ at $(v, v')$ if there is $t_0$ with $J_t(v, v') = A$ for all $|t| \geq |t_0|$. An eventual value is unique, since two such constants agree for $|t|$ large.

**Theorem 1.14.2 (Inputs on the regularized integral).** Let $\tau$, $\tau'$ be smooth, let $B$ be an $s$-twisted pairing for $P_{n+2}$, and let $c$ be a conductor of $\psi$.

1. If $B$ has eventual values $A_1$ at $(v_1, v')$ and $A_2$ at $(v_2, v')$, it has eventual value $A_1 + A_2$ at $(v_1 + v_2, v')$, and $zA_1$ at $(zv_1, v')$. The same holds in the second variable.
2. For all $v$, $v'$ there is an eventual value at $(v, v')$.
3. If $A$ is the eventual value at $(v, v')$ and $y \in k^{n+1}$, then the eventual value at $(\tau(u_y)v, v')$ is $\psi(y_{n+1})A$, and the eventual value at $(v, \tau'(u_y)v')$ is $\psi(-y_{n+1})A$.
4. If $A$ is the eventual value at $(v, v')$ and $p \in P_{n+1}$, then the eventual value at $(\tau(p)v, \tau'(p)v')$ is $|\det p|^{s+1}A$. Here $p$ acts through $\mathrm{diag}(p, 1)$.
5. If $B$ is left nondegenerate and $v \notin V(U_{n+2}, \theta_\psi)$, there is $v'$ at which the eventual value is nonzero.
6. Let $B_0$ be a bilinear form on $V \times V'$ with the transformation rules of items 3 and 4, such that for every $v \notin V(U_{n+2}, \theta_\psi)$ some $v'$ has $B_0(v, v') \neq 0$. Then $B_0$ descends to a left nondegenerate $(s+1)$-twisted pairing between $\Phi^-_\psi\tau$ and $\Phi^-_{\psi^{-1}}\tau'$.

Here $V(U, \theta)$ is the span of the vectors $\tau(u)v - \theta(u)v$, the kernel of the map to the twisted Jacquet module. The regularized integral is the tool of Bernstein (1984). Item 4 is the change of variables $x \mapsto px$ on $D_t$; the Jacobian $|\det p|$ adds one to the twist. Items 2 and 5 use the smoothness of $\tau$ and $\tau'$ and the conductor of $\psi$. Item 6 is a direct check: by item 3 the form kills $V(U_{n+2}, \theta_\psi)$ on the left and $V'(U_{n+2}, \theta_{\psi^{-1}})$ on the right.

**Theorem 1.14.3 (Pairings through Φ).** Let $\tau$ and $\tau'$ be smooth representations of $P_{n+2}$, and let $B$ be a left nondegenerate $s$-twisted pairing between them. Then there is a left nondegenerate $(s+1)$-twisted pairing $B'$ between $\Phi^-_\psi\tau$ and $\Phi^-_{\psi^{-1}}\tau'$, for the group $P_{n+1}$.

Lean: `pairing_phi` (also `invariant_pairing_mirabolic_smooth`).

*Proof.* By input 2, every pair $(v, v')$ has an eventual value $B_0(v, v')$, and it is unique. By input 1, $B_0$ is bilinear. By inputs 3 and 4, $B_0$ has the transformation rules of input 6. By input 5, for every $v \notin V(U_{n+2}, \theta_\psi)$ some $v'$ has $B_0(v, v') \neq 0$. Input 6 gives $B'$. $\square$

In terms of the normalized functor $\Phi = \Phi^-\nu^{-1/2}$ of Section 5, the twist does not change. The two factors $\nu^{-1/2}$ contribute $|\det p|^{-1}$, which cancels the extra $1$.

### Iteration and derivatives

The last application of $\Phi^-$ is replaced by $\Psi^-$. This step needs the vanishing of the next $\Phi^-$, and it is an input.

**Theorem 1.14.4 (Pairings through Ψ when Φ vanishes).** Let $\tau$ and $\tau'$ be smooth representations of $P_{n+2}$, and let $B$ be a left nondegenerate $s$-twisted pairing. Assume $\Phi^-_\psi\tau = 0$. Then there is a left nondegenerate $s$-twisted pairing between $\Psi^-\tau$ and $\Psi^-\tau'$, for the group $G_{n+1}$.

This is the vanishing case of Bernstein's argument, Bernstein (1984). We use it as stated and do not reprove it here.

**Theorem 1.14.5 (Iterated pairings).** Let $j, s \in \mathbb{N}$. Let $\tau$ and $\tau'$ be smooth representations of $P_{n+j+2}$, and let $B$ be a left nondegenerate $s$-twisted pairing between them. Assume
$$\Phi^-_\psi\big((\Phi^-_\psi)^j\tau\big) = 0.$$
Then there is a left nondegenerate $(s+j)$-twisted pairing between $\Psi^-(\Phi^-_\psi)^j\tau$ and $\Psi^-(\Phi^-_{\psi^{-1}})^j\tau'$, for the group $G_{n+1}$.

Lean: `pair_iter`.

*Proof.* Induction on $j$, for all $s$, $\tau$ and $\tau'$ at once. For $j = 0$ the claim is the theorem on pairings through $\Psi$. Let $j \geq 0$ and assume the claim for $j$. Let $\tau$, $\tau'$ be representations of $P_{n+j+3}$ with $\Phi^-_\psi(\Phi^-_\psi)^{j+1}\tau = 0$. The theorem on pairings through $\Phi$ gives a left nondegenerate $(s+1)$-twisted pairing $B_1$ between $\Phi^-_\psi\tau$ and $\Phi^-_{\psi^{-1}}\tau'$, for $P_{n+j+2}$. These two representations are smooth, since $\Phi^-$ keeps smoothness. Now $(\Phi^-_\psi)^{j+1}\tau = (\Phi^-_\psi)^j(\Phi^-_\psi\tau)$, and the same holds for $\tau'$ with $\psi^{-1}$. The claim for $j$, applied to $\Phi^-_\psi\tau$, $\Phi^-_{\psi^{-1}}\tau'$, $B_1$ and $s + 1$, gives a pairing with twist $(s + 1) + j = s + (j + 1)$. $\square$

**Theorem 1.14.6 (Pairings on derivatives).** Let $n, j \in \mathbb{N}$ and $N = n + j + 2$. Let $\pi$ and $\pi'$ be smooth representations of $G_N$ on $V$ and $V'$, and let $B$ be a $G_N$-invariant bilinear form on $V \times V'$ which is left nondegenerate. Assume
$$\Phi^-_\psi\big((\Phi^-_\psi)^j(\pi|_{P_N})\big) = 0.$$
Then there is a left nondegenerate bilinear form $B'$ on $\pi^{(j+1)}_\psi \times \pi'^{(j+1)}_{\psi^{-1}}$ with
$$B'(g w, g w') = |\det g|^{j}\,B'(w, w') \qquad (g \in G_{n+1}).$$

Lean: `pair_deriv`.

*Proof.* The restrictions $\pi|_{P_N}$ and $\pi'|_{P_N}$ are smooth, and $B$ is a $0$-twisted pairing between them. The theorem on iterated pairings with $s = 0$ gives the claim. $\square$

The hypothesis says that $(\Phi^-_\psi)^{j+1}(\pi|_{P_N}) = 0$, so $\pi^{(j+1)}$ is the last derivative that can be nonzero: it is the highest derivative of $\pi$. For an irreducible unitary $\pi$ take $\pi' = \bar{\pi}$, the complex conjugate representation, and $B$ the invariant inner product. Then $\bar{\pi}^{(j+1)}_{\psi^{-1}}$ is the complex conjugate of $\pi^{(j+1)}_\psi$, and $B'$ is a nondegenerate invariant Hermitian form on the twist $\pi^{(j+1)}\nu^{j/2}$. In normalized terms the twist by $\nu^{j/2}$ becomes a twist by $\nu^{1/2}$, since the normalized derivative is $\pi^{(j+1)}\nu^{-(j+1)/2}$. Bernstein (1984) proves that the highest derivative of an irreducible unitary representation, twisted by $\nu^{1/2}$, is unitary. The theorem above gives the invariant Hermitian form in that statement; it says nothing about positivity.

**Remark 1.14.7 (Formalization).** The three theorems are in [InvariantPairingMirabolicSmooth.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/InvariantPairingMirabolicSmooth.lean#L22) and [IsSmoothIterPhi.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/IsSmoothIterPhi.lean#L128). The group $P_{n+2}$ is `Mir k (n+1)`. The inputs are `mirabolic_evaluation_linear`, `mirabolic_pairing_exists_eventual_value`, `mirabolic_pairing_depth_induction`, `mirabolic_pairing_conductor_shift`, `mirabolic_pairing_conductor_extension` and `twisted_invariant_pairing_character`, whose statements we opened. The eventual value is `EvVal` and the integral $J_t$ is `JJ`, in [ShearGL.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/ShearGL.lean#L45). The existence of eventual values is stated in `MirabolicPairingConductorVanishingStatement.lean`, whose name does not match its content. The base case of the induction is `invariant_pairing_mirabolic_vanishing`, proved by `pair_psi`; it is not one of the results of this chapter, and we state it above as an input. The vanishing hypothesis is written as `Subsingleton` of a twisted Jacquet module. The proofs of `pair_iter` and `pair_deriv` run under `maxHeartbeats 2000000` (L126 and L150), and the wrapper `invariant_pairing_mirabolic_smooth` is proved by `first | exact …` under `maxHeartbeats 1000000`.
