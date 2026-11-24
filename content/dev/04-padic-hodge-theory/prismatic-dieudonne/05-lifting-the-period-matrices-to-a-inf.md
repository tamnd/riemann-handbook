---
title: Lifting the period matrices to A_inf
decls:
  - GlobalTheory.WinLift.Top.window_lift
  - GlobalTheory.T.window_lift_to_fontaineAinf_matrices
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lifting the period matrices to $A_{\inf}$

This section proves that the matrices $U$, $Y$ and $G_m$ of [the last section](/entry/window-matrices/) over a frame over $A_{\inf}$ come from matrices over $A_{\inf}$ itself. The output is a pair of matrices $F_a$ and $G_a$ over $A_{\inf}$ with $G_a F_a = \mu \cdot 1$, a matrix $\Psi$ with $F_a = \Psi\, \varphi^{-1}(F_a)$ that is invertible up to $\xi$, and the same images under $\theta$ as $Y$ and $G_m$. These are the defining relations of the Hodge-Tate datum of the next section ([Theorem 5.6.3](/entry/has-datum-of-conn-dual-conn/)), and through it of the theorem on prismatic Dieudonné modules ([Theorem 2.8.5 of Volume 12](/entry/prismatic-dieudonne-hodge/)).

We keep the notation of the last two sections. The Frobenius $\varphi$ of $A_{\inf} = W(O^\flat)$ is bijective, since $O^\flat$ is perfect of characteristic $p$. Let $\varphi^{-1}$ be its inverse; it is the map of Witt vectors induced by the inverse of the Frobenius of $O^\flat$. Let $\varepsilon \in O^\flat$ and let $\varepsilon^{1/p}$ be its unique $p$-th root. Put
$$\begin{aligned}
\mu &= [\varepsilon] - 1, & \nu &= [\varepsilon^{1/p}] - 1, & \xi &= \sum_{i < p} [\varepsilon^{1/p}]^i.
\end{aligned}$$
Then $\xi \nu = \mu$ by the geometric sum, and $\varphi^{-1}(\mu) = \nu$. Also $\varphi(\mu) = \mu\, \varphi(\xi)$, since $\varphi(\xi) = \sum_{i<p} [\varepsilon]^i$. If $\varepsilon$ is a primitive system, then $\theta(\mu) = 0$, since the $0$-th component of $\varepsilon$ is $1$, and $\theta(\varphi(\xi)) = p$. For matrices over $A_{\inf}$, $\varphi$ and $\varphi^{-1}$ act entry by entry. For matrices over a frame we write $a$, $\theta$ and $\sigma$ entry by entry in the same way. Put $\Delta = \mathrm{diag}_{d,k}(p, 1)$ and $\Delta' = \mathrm{diag}_{d,k}(1, p)$, over $B$ or over $A_{\inf}$.

**Theorem 5.5.1 (Lifting to $A_{\inf}$).** Let $p$, $C$, $v$ and $O$ be as in the first section, let $\varepsilon \in O^\flat$ be a primitive system, and let $(B, Q, a, \theta, \sigma, s, \tau)$ be a frame over $A_{\inf}$ for $\varepsilon$. Let $d, k, h \geq 0$. Let $U$ be a square matrix over $B$ of size $d + k$, let $Y$ be a matrix over $B$ with rows indexed by $\{1, \ldots, d\} \sqcup \{1, \ldots, k\}$ and $h$ columns, and let $G_m$ be a matrix over $B$ with $h$ rows and columns indexed like the rows of $Y$. Assume:

1. $U$ is invertible;
2. $\sigma(Y) = \Delta\, U^{T}\, Y$;
3. $U \Delta\, \sigma(G_m^{T}) = p\, G_m^{T}$;
4. $G_m Y = a(\mu) \cdot 1_h$;
5. $\theta(Y_{(1,i), m}) = 0$ for all $i$ and $m$, and $\theta((G_m)_{m, (2,j)}) = 0$ for all $m$ and $j$;
6. $U \Delta$ and $(U^{T})^{-1} \Delta'$ are nilpotent modulo the maximal ideal for $\theta$ and $\sigma$.

Then there are matrices $F_a$ over $A_{\inf}$ of the shape of $Y$, $G_a$ over $A_{\inf}$ of the shape of $G_m$, and square matrices $\Psi$ and $\Psi'$ over $A_{\inf}$ of size $d + k$, such that:

1. $G_a F_a = \mu \cdot 1_h$;
2. $F_a = \Psi\, \varphi^{-1}(F_a)$;
3. $\Psi \Psi' = \xi \cdot 1_{d+k}$;
4. $\theta(F_a) = \theta(Y)$ and $\theta(G_a) = \theta(G_m)$ entry by entry.

Lean: `GlobalTheory.WinLift.Top.window_lift` (also `GlobalTheory.T.window_lift_to_fontaineAinf_matrices`, a wrapper).

The hypotheses are parts 1 to 6 of the theorem on [period matrices](/entry/window-matrices/), with $h$ free. The proof lifts $U$ and solves two Frobenius equations over $A_{\inf}$ by successive approximation. It then compares the solutions with $Y$ and $G_m$ over the frame. We take as given the results on frames over $A_{\inf}$ that are named in the steps below.

*Proof.* Put $\xi' = \varphi(\xi)$. The ring $A_{\inf}$ is a domain. Also $\xi' \neq 0$, since $\theta(\xi') = p$ is not $0$ in $C$. Also $\theta(\tau) = 0$: the relation $p \tau = a(\mu)$ gives $p\, \theta(\tau) = \theta(\mu) = 0$, and $O$ has no $p$-torsion. If $\mu$ divides $x$, then $\tau$ divides $a(x)$, since $a(\mu) = p \tau$.

1. *Lift of $U$.* We take as given that an invertible matrix over $B$ is congruent modulo $\tau$ to $a(V)$ for an invertible matrix $V$ over $A_{\inf}$. Choose such a $V$ for $U$.
2. *First approximations.* Every element of $B$ has the form $a(x) + \tau a(y)$. So there are matrices $F_0$, $F_1$ over $A_{\inf}$ of the shape of $Y$ with $Y = a(F_0) + \tau a(F_1)$, and matrices $G_0$, $G_1$ of the shape of $G_m^T$ with $G_m^{T} = a(G_0) + \tau a(G_1)$. Then $Y \equiv a(F_0)$ and $G_m^T \equiv a(G_0)$ modulo $\tau$, and $\theta(F_0) = \theta(Y)$ and $\theta(G_0) = \theta(G_m^T)$, since $\theta(\tau) = 0$.
3. *Equations modulo $\mu$.* We take as given: if $R \equiv a(R_0)$, $S \equiv a(S_0)$ and $Y \equiv a(F_0)$ modulo $\tau$, and $R\, \sigma(Y) = S Y$, then $R_0\, \varphi(F_0) - S_0 F_0$ is divisible by $\mu$ entry by entry. With $R = 1$ and $S = \Delta U^T$, hypothesis 2 gives that $\mu$ divides $\varphi(F_0) - \Delta V^T F_0$. With $R = U \Delta$ and $S = p \cdot 1$, hypothesis 3 gives that $\mu$ divides $V \Delta\, \varphi(G_0) - p\, G_0$.
4. *Equations modulo $\xi' \mu$.* We take as given two results that use hypothesis 5. Since $\theta$ is $0$ on the first block of $F_0$, the matrix $(V^T)^{-1} \mathrm{diag}_{d,k}(1, \xi')\, \varphi(F_0) - \xi' F_0$ is divisible by $\xi' \mu$. Since $\theta$ is $0$ on the second block of $G_0$, the matrix $V\, \mathrm{diag}_{d,k}(\xi', 1)\, \varphi(G_0) - \xi' G_0$ is divisible by $\xi' \mu$. We also take as given that hypothesis 6 makes $N_F = (V^T)^{-1} \mathrm{diag}_{d,k}(1, \xi')$ and $N_G = V\, \mathrm{diag}_{d,k}(\xi', 1)$ nilpotent modulo the maximal ideal for $\theta$ and $\varphi$: the first one uses $(U^T)^{-1} \Delta'$ and the second uses $U \Delta$.
5. *Solutions over $A_{\inf}$.* We take as given the successive approximation result: if $N$ is nilpotent modulo the maximal ideal for $\theta$ and $\varphi$, and $N \varphi(v_0) - \xi' v_0$ is divisible by $\xi' \mu$, then there is $w$ with $w \equiv v_0$ modulo $\mu$ and $\xi' w = N \varphi(w)$. Apply it to each column of $F_0$ with $N_F$, and let $F_a$ be the matrix of the solutions. Apply it to each column of $G_0$ with $N_G$, and let $G_a$ be the transpose of the matrix of the solutions. So $F_a \equiv F_0$ and $G_a^T \equiv G_0$ modulo $\mu$, and
$$\begin{aligned}
\xi' F_a &= (V^T)^{-1} \mathrm{diag}_{d,k}(1, \xi')\, \varphi(F_a), \\
\xi' G_a^T &= V\, \mathrm{diag}_{d,k}(\xi', 1)\, \varphi(G_a^T).
\end{aligned}$$
6. *The matrix $\Psi$.* Multiply the first equation by $\mathrm{diag}_{d,k}(\xi', 1)\, V^T$ on the left. Since $\mathrm{diag}_{d,k}(\xi', 1)\, \mathrm{diag}_{d,k}(1, \xi') = \xi' \cdot 1$, this gives $\xi'\, \mathrm{diag}_{d,k}(\xi', 1) V^T F_a = \xi' \varphi(F_a)$. Since $A_{\inf}$ is a domain and $\xi' \neq 0$, we get $\varphi(F_a) = \mathrm{diag}_{d,k}(\xi', 1)\, V^T F_a$. Put
$$\begin{aligned}
\Psi &= \varphi^{-1}\big(\mathrm{diag}_{d,k}(\xi', 1)\, V^T\big), & \Psi' &= \varphi^{-1}\big((V^T)^{-1} \mathrm{diag}_{d,k}(1, \xi')\big).
\end{aligned}$$
Then $\varphi(\Psi\, \varphi^{-1}(F_a)) = \mathrm{diag}_{d,k}(\xi', 1)\, V^T F_a = \varphi(F_a)$. Since $\varphi$ is injective, $F_a = \Psi\, \varphi^{-1}(F_a)$, which is part 2. Also $\Psi \Psi' = \varphi^{-1}(\xi' \cdot 1) = \xi \cdot 1$, which is part 3.
7. *Frobenius on $G_a F_a$.* Transpose the second equation: $\xi' G_a = \varphi(G_a)\, \mathrm{diag}_{d,k}(\xi', 1)\, V^T$. With step 6 this gives $\varphi(G_a F_a) = \varphi(G_a)\, \mathrm{diag}_{d,k}(\xi', 1)\, V^T F_a = \xi' G_a F_a$. So each entry of $G_a F_a$ is an eigenvector of $\varphi$ with eigenvalue $\xi'$. So is $\mu$, since $\varphi(\mu) = \xi' \mu$.
8. *A second Frobenius matrix.* We take as given that $a(\xi') = p u$ for a unit $u$ of $B$ with $u \equiv 1$ modulo $\tau$, and that there is $l \in B$ with $l \equiv 1$ modulo $\tau$ and $\sigma(l) = u l$. Put $U' = a(V)\, \mathrm{diag}_{d,k}(u, 1)$. Then $U'$ is invertible and $U' \equiv U$ modulo $\tau$, since $U \equiv a(V)$ and $u \equiv 1$. We take as given that two invertible matrices that are congruent modulo $\tau$, with $U\Delta$ nilpotent modulo the maximal ideal, give isomorphic windows: there is $X \equiv 1$ modulo $\tau$ with $X U' \Delta = U \Delta\, \sigma(X)$. The images of $U$ and $U'$ under $\theta$ are equal, since $\theta(\tau) = 0$. Nilpotence modulo the maximal ideal depends only on the image of the matrix under $\theta$, by a result we take as given. So $U' \Delta$ and $(U'^{T})^{-1} \Delta'$ are nilpotent modulo the maximal ideal.
9. *Comparison over the frame.* Put $Z = a(F_a)$ and $W = a(G_a^T)$. Since $\sigma \circ a = a \circ \varphi$, step 6 gives $\sigma(Z) = \mathrm{diag}_{d,k}(p u, 1)\, a(V)^T Z = \Delta\, U'^T Z$. Step 5 gives $U' \Delta\, \sigma(W) = p u\, W$. Also $Z \equiv Y$ and $W \equiv G_m^T$ modulo $\tau$, since $F_a \equiv F_0$ and $G_a^T \equiv G_0$ modulo $\mu$. We take as given two uniqueness results for such equations over the frame. With hypothesis 2, the first gives $Z = X^T Y$. With hypothesis 3 and the element $l$, the second gives $X W = l\, G_m^T$. So
$$\begin{aligned}
a(G_a F_a) = W^T Z = W^T X^T Y = (X W)^T Y = l\, G_m Y = l\, a(\mu) \cdot 1_h,
\end{aligned}$$
by hypothesis 4. Write $l = 1 + \tau c$. Then $\tau\, a(\mu) = p \tau^2 = 0$, so $l\, a(\mu) = a(\mu)$, and $a(G_a F_a) = a(\mu \cdot 1_h)$.
10. *Part 1.* We take as given that two eigenvectors of $\varphi$ with eigenvalue $\xi'$ that have the same image under $a$ are equal. By steps 7 and 9 this applies to each entry of $G_a F_a$ and of $\mu \cdot 1_h$. So $G_a F_a = \mu \cdot 1_h$.
11. *Part 4.* Write $F_a = F_0 + \mu c$. Then $\theta(F_a) = \theta(F_0) = \theta(Y)$, since $\theta(\mu) = 0$. In the same way $\theta(G_a) = \theta(G_0^T) = \theta(G_m)$. $\square$

The roles of the two Frobenius equations are dual. The matrix $F_a$ is a $\varphi$-equivariant map with matrix $\mathrm{diag}_{d,k}(\xi', 1)\, V^T$, so after $\varphi^{-1}$ its Frobenius matrix $\Psi$ has the form $\mathrm{diag}_{d,k}(\xi, 1)\, \varphi^{-1}(V^T)$. This is the shape of a Breuil-Kisin-Fargues module whose Frobenius is divisible by $\xi$ on the first block. The factor $u$ in step 8 measures the difference between $a(\varphi(\xi))$ and $p$ over the frame. The element $l$ absorbs it in the comparison for $G_m$.

**Remark 5.5.2 (Formalization).** The theorem is in [WindowLiftToFontaineAinfMatrices.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/WindowLiftToFontaineAinfMatrices.lean#L115). The results we take as given are the ten `GlobalTheory.T` statements bound at lines 29 to 47 of that file, and `frobenius_xi_eq_p_mul_unit`, `exists_ainf_frame_lift_twisted_frobenius` and `isIso_windows_of_matrix_congr_mod_tau` from their Statement files; we read their statements only. The transfer of nilpotence is `c_nilCong` at line 88, proved in the file from `isNil_of_theta_eq` in MuDvdFrobXiSub.lean. The elements $\xi$, $\nu$, $\mu$ and $\varphi^{-1}$ are `xi`, `nu`, `mu` and `phiInv` in [XiMulNu.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/XiMulNu.lean#L14). The statement leaves $h$ free; in its single use, `hasDatum_biconn_of` in HasDatumBiconnOf.lean, $h$ is the height. The proof finds the Frobenius equation of step 5 for $G_a$, but the conclusion records no Frobenius relation for $G_a$, and it does not say that $\Psi$ has the form $\mathrm{diag}_{d,k}(\xi, 1)\,\varphi^{-1}(V^T)$.
